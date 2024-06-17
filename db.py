from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase as Base

db = SQLAlchemy(model_class=Base)