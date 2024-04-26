import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(10))
    diameter = Column(String(10))
    rotation_period = Column(String(5))
    orbital_period = Column(String(10))
    gravity = Column(String(10))
    population = Column(String(20))
    climate = Column(String(20))
    terrain = Column(String(20))
    surface_water = Column(String(4))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    hair_color = Column(String(10))
    eye_color = Column(String(10))
    skin_color = Column(String(10))
    height = Column(String(3))
    weight = Column(String(20)) 
    gender = Column(String(10))
    year_of_birth = Column(String(10))
    homeworld_id = Column(Integer, ForeignKey('homeworld.id'))
    homeworld = relationship(Planet)

class FavoritePlanets(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    
class FavoriteCharacters(Base):
    __tablename__ = 'favorite_characters'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(30))
    password = Column(String(30))
    favorite_planets_id = Column(Integer, ForeignKey('favorite_planets.id'))
    favorite_planets = relationship(FavoritePlanets)
    favorite_characters_id = Column(Integer, ForeignKey('favorite_characters.id'))
    favorite_characters = relationship(FavoriteCharacters)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
