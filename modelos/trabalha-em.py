from sqlalchemy import Column, Integer, String

from modelos.base import Base

from datetime import time


class TrabalhaEm(Base.Base, Base):
    __tablename__ = "trabalha-em"
    nssEmpregado = Column(Integer, ForeignKey=True(nss))
    numeroProjeto = Column(Integer, ForeignKey=True(numeroprojeto))
    horas = Column (time(%h:%m:%s))