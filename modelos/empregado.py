from sqlalchemy import Column, Integer, String

from modelos.base import Base

from datetime import datetime


class Empregado(Base.Base, Base):
    __tablename__ = "empregado"
    nss = Column(Integer, primary_key=True, unique=True)
    pnome = Column(String, nullable=False)
    mnome = Column(String(50), unique=True,)
    snome = Column(String(50), unique=True,) 
    sexo = Column(String(15),nullable=False)
    dataNasc = Column(datetime, nullable=False)
    salario = Column(Integer)
    endereco = Column(String(50))
    numeroDepartamento = Column(Integer, unique=True)
    nssSupervisor = Column(Integer, ForeignKey=True(nss))
