from ..db_setup import Base

from sqlalchemy import Column, Integer, Text


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    email = Column(Text, unique=True, nullable=False, index=True, nullable=False)
    password = Column(Text, nullable=False)
