#!/usr/bin/python3
""" 0x02. AirBnB clone - MySQL, task 10. DBStorage - Amenity... and BOOM! """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .base_model import BaseModel, Base
from .place import place_amenity


class Amenity(BaseModel, Base):
    """ Defines attributes for `Amenity` as it inherits from `BaseModel`,
    and ORM properties in relation to table `amenities`.
    Attributes:
        name (Column): name of state, string of max 128 chars
        amenities (relationship): many-to-many-association to `Place`
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary=place_amenity)