from sqlalchemy import Column, Integer, String,Boolean,CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Empresa(Base):
    __tablename__ = 'empresas'
    id = Column(Integer, primary_key=True)
    cnpj = Column(CHAR(14), unique=True, nullable=False)
    razao_social = Column(String(100), nullable=False)
    ativo = Column(Boolean, default=True)