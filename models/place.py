#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 backref='places', viewonly=False)
    else:
        from . import storage  # here to avoid circular import

        @property
        def reviews(self):
            """Return list of Review instances with place_id equal to the
            current Place.id"""
            list_reviews = []
            for review in storage.all(Review).values():
                if self.id == review.place_id:
                    list_reviews.append(review)
            return list_reviews

        @property
        def amenities(self):
            """ Returns list of Amenity instances with `place_id` matching
            `self.id` """
            list_amenities = []
            for amenity in storage.all(Amenity).values():
                if self.id == amenity.place_id:
                    list_amenities.append(amenity)
            return list_amenities

        @amenities.setter
        def amenities(self, obj):
            """ Adds id of object to list `self.amenity_ids` if object is `Amenity`
            type """
            if type(obj) == 'Amenity':
                self.amenity_ids.append(obj.id)
