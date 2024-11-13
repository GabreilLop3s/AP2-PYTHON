from sqlalchemy import Column, Integer, String

from modelos.base import Base


class User(Base.Base, Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(50), nullable=False)
    email = Column(String(200), unique=True, nullable=False)
