from sqlalchemy import Column, Integer, String

from modelos.base import Base


class Empregado(Base.Base, Base):
    __tablename__ = "empregado"
    nss = Column(Integer, primary_key=True)
    pnome = Column(String, nullable=False)
    mnome = Column(String(50), unique=True,nullable=False)
    snome = Column(String(50), unique=True, nullable=False) 
    sexo = Column(String(15),nullable=False)
    dataNasc = Column()
    salario = Column#(<Domínio e restrições>)
    endereco = Column#(<Domínio e restrições>)
    numeroDepartamento = Column#(<Domínio e restrições>)
    nssSupervisor = Column#(<Domínio e restrições>)
