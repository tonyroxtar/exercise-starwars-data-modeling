import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

#class Person(Base):
#    __tablename__ = 'person'
#    # Here we define columns for the table person
#    # Notice that each column is also a normal Python instance attribute.
#    id = Column(Integer, primary_key=True)
#    name = Column(String(250), nullable=False)

#class Address(Base):
#    __tablename__ = 'address'
#    # Here we define columns for the table address.
#    # Notice that each column is also a normal Python instance attribute.
#    id = Column(Integer, primary_key=True)
#    street_name = Column(String(250))
#    street_number = Column(String(250))
#    post_code = Column(String(250), nullable=False)
#    person_id = Column(Integer, ForeignKey('person.id'))
#    person = relationship(Person)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    username = Column(String(20))
    name = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(100))
    password = Column(String(10))
    
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key = True)
    name = Column(String(20))
    system = Column(String(30))
    faction = Column(String(20))

class Ships(Base):
    __tablename__ = 'ships'
    id = Column(Integer, primary_key = True)
    name = Column(String(20))
    faction = Column(String(20))

class Characters(Base):
    __tablename__ = 'characters'
    id= Column(Integer, primary_key = True)
    name = Column(String(20))
    planet = Column(String, ForeignKey('planets.name'))
    ship = Column(String, ForeignKey('ships.name'))
    planet = relationship(Planets)
    ship = relationship(Ships)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    ship_id = Column(Integer, ForeignKey('ships.id'))
    user = relationship(User)
    character = relationship(Characters)
    planet = relationship(Planets)
    ship = relationship(Ships)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
