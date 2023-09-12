from sqlalchemy import Column, String

from db import Base


class User(Base):
    __tablename__ = "users"

    name = Column(String, nullable=False, unique=True, primary_key=True)