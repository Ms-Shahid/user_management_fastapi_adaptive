from sqlalchemy import Boolean, Column, Integer, String
from database import Base, engine

Base.metadata.create_all(engine)