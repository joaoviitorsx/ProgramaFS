from src.Models.c170Model import RegistroC170
from src.Config.Database.db import SessionLocal
from src.Services.estrutura.PNM.builderLinhaPNM import criarLinhaPNM

def exportarPNM(empresa_id: int, periodo: str) -> list[str]:
    session = SessionLocal()
    linhas = []

    try:
        registros = session.query(RegistroC170).filter_by(
            empresa_id=empresa_id,
            periodo=periodo,
            ativo=True
        ).all()

        for r in registros:
            campos = criarLinhaPNM(r)
            linha = "|" + "|".join(campos) + "|"
            linhas.append(linha)

    except Exception as e:
        print(f"❌ Erro ao exportar PNM: {e}")
    finally:
        session.close()

    return linhas