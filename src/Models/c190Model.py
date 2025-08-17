from sqlalchemy import Column, Integer, String,Boolean, DECIMAL
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class RegistroC190(Base):
    __tablename__ = 'c190'
    id = Column(Integer, primary_key=True)
    empresa_id = Column(Integer, nullable=False, index=True)
    periodo = Column(String(10), nullable=False)
    c100_id = Column(Integer, index=True)
    reg = Column(String(10), default='C190')
    cst_icms = Column(String(3))
    cfop = Column(String(10))
    aliq_icms = Column(DECIMAL(7,2))
    vl_opr = Column(DECIMAL(15,2))
    vl_bc_icms = Column(DECIMAL(15,2))
    vl_icms = Column(DECIMAL(15,2))
    vl_bc_icms_st = Column(DECIMAL(15,2))
    vl_icms_st = Column(DECIMAL(15,2))
    vl_red_bc = Column(DECIMAL(15,2))
    vl_ipi = Column(DECIMAL(15,2))
    cod_obs = Column(String(10))
    ativo = Column(Boolean, default=True)