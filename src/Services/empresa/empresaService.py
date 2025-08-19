import asyncio
from sqlalchemy.orm import Session
from src.Config.Database.db import SessionLocal
from src.Models.empresaModel import Empresa
from src.Utils.cnpj import buscarInformacoesApi

def obterOuCadastrarEmpresa(session: Session, cnpj: str) -> dict:
    empresa_existente = session.query(Empresa).filter_by(cnpj=cnpj).first()
    if empresa_existente:
        return {
            "status": "erro",
            "mensagem": "Empresa com esse CNPJ já está cadastrada.",
            "empresa_id": empresa_existente.id,
            "razao_social": empresa_existente.razao_social,
            "cnpj": empresa_existente.cnpj,
            "uf": empresa_existente.uf,
        }

    razao_social, _, uf, _, _ = asyncio.run(buscarInformacoesApi(cnpj))

    if not razao_social:
        return {"status": "erro", "mensagem": "Não foi possível consultar a razão social via API."}

    nova_empresa = Empresa(cnpj=cnpj, razao_social=razao_social, uf=uf)
    session.add(nova_empresa)
    session.commit()

    return {
        "status": "ok",
        "empresa_id": nova_empresa.id,
        "razao_social": nova_empresa.razao_social,
        "cnpj": nova_empresa.cnpj,
        "uf": nova_empresa.uf
    }


def listarEmpresas():
    with SessionLocal() as db:
        empresas = db.query(Empresa).all()
        return [{
            "id": e.id, 
            "razao_social": e.razao_social,
            "cnpj": e.cnpj,
            "uf": e.uf
            } for e in empresas]