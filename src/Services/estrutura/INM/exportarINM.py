from src.Models.inmModel import RegistroINM
from src.Config.Database.db import SessionLocal
from src.Services.estrutura.INM.builderLinhaINM import criarLinhaINM

def exportarINM(empresa_id, periodo):
    db = SessionLocal()
    linhas = []

    try:
        registros = db.query(RegistroINM).filter_by(empresa_id=empresa_id, periodo=periodo, ativo=True).all()
        for registro in registros:
            linha = criarLinhaINM(registro)
            linhas.append(linha)
    finally:
        db.close()

    return linhas