#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", cascade="all, delete, delete-orphan", backref="state")


@property
def cities(self, state_id):
    """Get a list of City instances with state_id equal to the given state_id"""
    cities_list = []
    all_cities = self.all(City)
    for city in all_cities.values():
        if getattr(city, 'state_id') == state_id:
            cities_list.append(city)
    return cities_list
