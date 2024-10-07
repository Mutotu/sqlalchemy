from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Table

Base = declarative_base()

class User(Base):
  __tablename__= 'users'
  pets = relationship('Pet', back_populates='user', cascade="all, delete, delete-orphan")
  id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
  name = Column(String, nullable=False)
  email = Column(String)
  nickname = Column(String(50))

  def __repr__(self):
    return f'<User(id={self.id} name="{self.name} email="{self.email} nickname="{self.nickname}")>'

class Pet(Base):
  __tablename__ = 'pets'

  id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
  name = Column(String, nullable=False)
  species = Column(String, nullable=False)
  age = Column(Integer)
  user_id = Column(ForeignKey('users.id'))

  user = relationship('User', back_populates='pets')
  # pet_toys = Table('pet_toys', Base.metadata,
  #                  Column('pet_id', ForeignKey('pets.id'),
  #                         primary_key=True), Column('toys_id',
  #                                                   ForeignKey('toys.id'),
  #                                                   primary_key=True)
  #                  )

  # toys = relationship('Toy', secondary=pet_toys, back_populates='pets')

  def __repr__(self):
    return f'<Pet(id={self.id} name="{self.name} species="{self.species} age={self.age} user_id={self.user_id})>'
# class Toy(Base):
#   __tablename__ = 'toys'
#
#   id = Column(Integer, Sequence('toy_id_seq'), primary_key=True)
#   toy = Column(String(50), nullable=False, unique=True)
#
#   # pets = relationship('Pet', secondary=pet_toys, back_populates='toys')
#
#   def __repr__(self):
#     return f'<Toy(id={self.id}, toy="{self.toy}")'

engine = create_engine('sqlite:///:memory:', echo=True)

# To migrate everything (create tables based on your models)
Base.metadata.create_all(engine)