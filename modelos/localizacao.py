from sqlalchemy import Column, Integer, String

from modelos.base import Base


class Localizacao(Base.Base, Base):
    __tablename__ = "localizacao"
    localizacao = Column(String(50))
    numeroDepartamento = Column(Integer, ForeignKey=True(numeroDepart))
