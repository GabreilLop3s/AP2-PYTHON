from sqlalchemy import Column, Integer, String

from modelos.base import Base


class Projeto(Base.Base, Base):
    __tablename__ = "projeto"
    numeroProjeto = Column(Integer, primary_key=True)
    nome = Column#(<Domínio e restrições>)
    localizacao = Column#(<Domínio e restrições>)
    numeroDepartamento = Column#(<Domínio e restrições>)