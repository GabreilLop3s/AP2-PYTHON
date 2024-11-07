from sqlalchemy import Column, Integer, String

from modelos.base import Base


class Departamento(Base.Base, Base):
    __tablename__ = "departamento"
    numero = Column(Integer,primary_key=True)
    nome = Column(String(50),unique=True, nullable=False )
    numeroEmpregado = Column(Integer, )
    nssEmpregrado = Column#(<Domínio e restrições>)
    dataInicio = Column#(<Domínio e restrições>)

