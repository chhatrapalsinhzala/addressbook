from sqlalchemy import Column, Integer, Float, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Address(Base):

    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True, index =True)
    title = Column(String)
    longitude = Column(Float)
    latitude = Column(Float)
    city = Column(String)
    state = Column(String)
    country = Column(String)

    user_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates="addresses")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    addresses = relationship('Address', back_populates="owner")