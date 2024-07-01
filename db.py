from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """
    This subclass of DeclarativeBase is needed otherwise SQL Alchemy will have an issue with the primary mapper.
    Using DeclarativeBase directly caused an error in mapping.

    For example: 
    `sqlalchemy.exc.ArgumentError: Class '<class 'shortener.models.Url'>' already has a primary mapper defined.`
    """
    pass

db = SQLAlchemy(model_class=Base)