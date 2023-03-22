#!/usr/bin/python3
"""
This module contains the City class for the HBNB project.
"""

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    This class defines a City object that inherits from BaseModel and Base.
    It corresponds to the "cities" table in the MySQL database.
    """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship('Place', backref='cities',
                          cascade='all, delete-orphan')
