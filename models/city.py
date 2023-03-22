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
    __tablename__ = "cities"

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")

    def __init__(self, *args, **kwargs):
        """
        Initializes a new City object with the given parameters.
        """
        super().__init__(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the City object.
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
