#!/usr/bin/python3

"""
SQLAlchemy object-relational configuration involves the combination
of Table, mapper(), and class objects to define a mapped class.
declarative allows all three to be expressed at once within the class declaration.
The declarative_base() callable returns a new base class from which
all mapped classes should inherit. When the class definition is completed,
a new Table and mapper() will have been generated.
The resulting table and mapper are accessible via __table__ and __mapper__
attributes on the State class. e.g to access mapped table: state.__table__
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    class inherits from base, and links to the mysql table 'states'.
    class attribute id is a column of auto generated, unique integer,
    cant be null, and is a primary key.
    class attribute name is a column of string with max 128 characters,
    and cant be null.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
