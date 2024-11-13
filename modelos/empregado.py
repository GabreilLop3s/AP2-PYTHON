from sqlalchemy import Column, Integer, String, ForeignKey, FLOAT, DateTime

from modelos.base import Base

from sqlalchemy.orm import relationship

from departamento import Departamento


class Empregado(Base.Base, Base):
    __tablename__ = "empregado"
    nss = Column(Integer, primary_key=True, unique=True)
    pnome = Column(String(50), nullable=False)
    mnome = Column(String(50), unique=True,nullable=False)
    snome = Column(String(50), unique=True,nullable=False) 
    sexo = Column(String(15),nullable=False, nullable=False)
    dataNasc = Column(DateTime, nullable=False)
    salario = Column(FLOAT, nullable=False)
    endereco = Column(String(50))
    numeroDepartamento = Column(Integer, ForeignKey('Departamento.numeroDepart'),unique=True)
    nssSupervisor = Column(Integer, ForeignKey(nss))
