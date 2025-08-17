from sqlalchemy import Column, Integer,Boolean, DECIMAL, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SNM(Base):
    __tablename__ = 'snm'
    id = Column(Integer, primary_key=True)
    empresa_id = Column(Integer, nullable=False, index=True)
    c170_id = Column(Integer, index=True)
    tipo_st = Column(Integer)
    custo_aquisicao = Column(DECIMAL(15,4))
    perc_agregacao = Column(DECIMAL(7,2))
    base_st = Column(DECIMAL(15,2))
    aliq_icms = Column(DECIMAL(7,2))
    valor_st = Column(DECIMAL(15,2))
    valor_credito = Column(DECIMAL(15,2))
    valor_antecipado = Column(DECIMAL(15,2))
    indicador_fecop = Column(CHAR(1))
    ativo = Column(Boolean, default=True)