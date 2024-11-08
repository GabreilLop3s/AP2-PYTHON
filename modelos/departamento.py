from sqlalchemy import Column, Integer, String

from modelos.base import Base

from datetime import datetime


class Departamento(Base.Base, Base):
    __tablename__ = "departamento"
    numeroDepart = Column(Integer,primary_key=True, unique=True)
    nome = Column(String(50),unique=True, nullable=False)
    numeroEmpregado = Column(Integer,nullable=False, unique=True)
    nssEmpregrado = Column(Integer,ForeignKey=True(nss))
    dataInicio = Column(datetime())

