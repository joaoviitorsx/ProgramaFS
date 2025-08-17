from sqlalchemy import Column, Integer, String,Boolean,CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Registro0150(Base):
    __tablename__ = '0150'
    id = Column(Integer, primary_key=True)
    empresa_id = Column(Integer, index=True)
    reg = Column(String(10))
    cod_part = Column(String(60))
    nome = Column(String(100))
    cod_pais = Column(String(10))
    cnpj = Column(CHAR(14))
    cpf = Column(CHAR(11))
    ie = Column(String(20))
    cod_mun = Column(String(20))
    suframa = Column(String(20))
    ende = Column(String(100))
    num = Column(String(20))
    compl = Column(String(20))
    bairro = Column(String(50))
    uf = Column(CHAR(2))
    tipo_pessoa = Column(CHAR(1))
    periodo = Column(String(10))
    ativo = Column(Boolean, default=True)