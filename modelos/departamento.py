from sqlalchemy import Column, Integer, String

from modelos.base import Base

from datetime import datetime


class Departamento(Base.Base, Base):
    __tablename__ = "departamento"
    numero = Column(Integer,primary_key=True)
    nome = Column(String(50),unique=True, nullable=False)
    numeroEmpregado = Column(Integer,nullable=False)
    nssEmpregrado = Column(Integer,ForeignKey(nss) )
    dataInicio = Column(datetime())

