from sqlalchemy.exc import SQLAlchemyError
from src.Services.empresa.empresaService import obterOuCadastrarEmpresa, listarEmpresas
from src.Config.Database.db import SessionLocal

def cadastrarEmpresa(cnpj: str) -> dict:
    session = SessionLocal()
    try:
        return obterOuCadastrarEmpresa(session, cnpj)
    except SQLAlchemyError as e:
        session.rollback()
        return {"status": "erro", "mensagem": str(e)}
    finally:
        session.close()

def obterEmpresas():
    try:
        return listarEmpresas()
    except Exception as e:
        print(f"[Erro] Falha ao listar empresas: {e}")
        return []