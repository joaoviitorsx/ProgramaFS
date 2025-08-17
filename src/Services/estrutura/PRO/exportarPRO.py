from src.Models._0200Model import Registro0200
from src.Config.Database.db import SessionLocal
from src.Services.estrutura.PRO.builderLinhaPRO import criarLinhaPRO

def exportarPRO(empresa_id: int, periodo: str) -> list[str]:
    session = SessionLocal()
    linhas = []

    try:
        produtos = session.query(Registro0200).filter_by(
            empresa_id=empresa_id,
            periodo=periodo,
            ativo=True
        ).all()

        for p in produtos:
            campos = criarLinhaPRO(p)
            linha = "|" + "|".join(campos) + "|"
            linhas.append(linha)

    except Exception as e:
        print(f"❌ Erro ao exportar PRO: {e}")
    finally:
        session.close()

    return linhas