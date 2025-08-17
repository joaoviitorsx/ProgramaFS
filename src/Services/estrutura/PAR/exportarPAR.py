from src.Models._0150Model import Registro0150
from src.Config.Database.db import SessionLocal
from src.Services.estrutura.PAR.builderLinhaPAR import criarLinhaPAR

def exportarPAR(empresa_id: int, periodo: str) -> list[str]:
    session = SessionLocal()
    linhas = []

    try:
        participantes = session.query(Registro0150).filter_by(
            empresa_id=empresa_id,
            periodo=periodo,
            ativo=True
        ).all()

        for p in participantes:
            campos = criarLinhaPAR(p)
            linha = "|" + "|".join(campos) + "|"
            linhas.append(linha)

    except Exception as e:
        print(f"❌ Erro ao exportar PAR: {e}")
    finally:
        session.close()

    return linhas