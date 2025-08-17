from sqlalchemy import Column, Integer, String, Date, Boolean,CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Registro0000(Base):
    __tablename__ = '0000'
    id = Column(Integer, primary_key=True)
    empresa_id = Column(Integer, index=True)
    reg = Column(String(10))
    cod_ver = Column(String(10))
    cod_fin = Column(String(10))
    dt_ini = Column(Date)
    dt_fin = Column(Date)
    nome = Column(String(100))
    cnpj = Column(CHAR(14))
    cpf = Column(CHAR(11))
    uf = Column(CHAR(2))
    ie = Column(String(20))
    cod_num = Column(String(20))
    im = Column(String(20))
    suframa = Column(String(20))
    ind_perfil = Column(String(10))
    ind_ativ = Column(String(10))
    filial = Column(String(10))
    periodo = Column(String(10))
    ativo = Column(Boolean, default=True)
