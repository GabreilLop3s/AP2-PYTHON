from sqlalchemy import Column, Integer, String

from modelos.base import Base


class Projeto(Base.Base, Base):
    __tablename__ = "projeto"
    numeroProjeto = Column(Integer, primary_key=True, unique=True)
    nome = Column(String(50), nullable=False)
    localizacao = Column(String(50))
    numeroDepartamento = Column(Integer, ForeignKey=True(numeroDepart))