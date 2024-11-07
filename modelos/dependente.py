from sqlalchemy import Column, Integer, String

from modelos.base import Base

from datetime import datetime


class Dependente(Base.Base, Base):
    __tablename__ = "dependente"
    nssEmpregado = Column(Integer, ForeignKey(nss))
    nome = Column(String(50))
    sexo = Column(String(15))
    dataNasc = Column(datetime)
    tipoRelacionamento = Column(String(50))