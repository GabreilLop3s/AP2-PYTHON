from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from modelos.base import Base

from modelos.empregado import Empregado

from sqlalchemy.orm import relationship



class Dependente(Base.Base, Base):
    __tablename__ = "dependente"
    nssEmpregado = Column(Integer,ForeignKey('Empregado.nss'),unique=True, primary_key=True)
    nome = Column(String(50))
    sexo = Column(String(15))
    dataNasc = Column(DateTime)
    tipoRelacionamento = Column(String(50))