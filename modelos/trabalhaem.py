from sqlalchemy import Column, Integer, ForeignKey, DateTime

from modelos.base import Base

from modelos.projeto import Projeto

from modelos.empregado import Empregado

from sqlalchemy.orm import relationship


class TrabalhaEm(Base.Base, Base):
    __tablename__ = "trabalha-em"
    nssEmpregado = Column(Integer, ForeignKey('Empregado.nss'))
    numeroProjeto = Column(Integer, ForeignKey('Projeto.numeroProjeto'))
    horas = Column (DateTime())