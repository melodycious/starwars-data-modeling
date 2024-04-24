import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False) 
    fist_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250))


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250)) 
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    gravity = Column(String(250))
    orbital_period = Column(Integer)


class People(Base):
    __tablename__ = 'people'
    ID = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))


class FavoritePeople(Base):
    __tablename__ = 'favorite_people'
    ID = Column(Integer, primary_key=True)
    user_ID = Column(Integer, ForeignKey('user.ID'))
    user_relationship = relationship(User)
    character_id = Column(Integer, ForeignKey('character.ID'))
    character_relationship = relationship(People) 


class FavouritePlanets(Base):
    __tablename__= 'favorite_planets'
    ID = Column(Integer, primary_key=True)
    user_ID = Column(Integer, ForeignKey('user.ID'))
    user_relationship = relationship(User)
    planets_id = Column(Integer, ForeignKey('planets.ID'))
    planets_relationship = relationship(Planets)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
