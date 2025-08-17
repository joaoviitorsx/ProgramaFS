from src.Models.snmModel import RegistroSNM
from src.Config.Database.db import SessionLocal
from src.Services.estrutura.SNM.builderLinhaSNM import criarLinhaSNM

def exportarSNM(empresa_id: int, periodo: str) -> list[str]:
    session = SessionLocal()
    linhas = []

    try:
        registros = session.query(RegistroSNM).filter_by(
            empresa_id=empresa_id,
            periodo=periodo,
            ativo=True
        ).all()

        for r in registros:
            campos = criarLinhaSNM(r)
            linha = "|" + "|".join(campos) + "|"
            linhas.append(linha)

    except Exception as e:
        print(f"❌ Erro ao exportar SNM: {e}")
    finally:
        session.close()

    return linhas