from src.Models.nfmModel import RegistroNFM
from src.Config.Database.db import SessionLocal
from src.Services.estrutura.NFM.builderLinhaNFM import criarLinhaNFM

def exportarNFM(empresa_id: int, periodo: str) -> list[str]:
    session = SessionLocal()
    linhas = []

    try:
        notas = session.query(RegistroNFM).filter_by(
            empresa_id=empresa_id,
            periodo=periodo,
            ativo=True
        ).all()

        for n in notas:
            campos = criarLinhaNFM(n)
            linha = "|" + "|".join(campos) + "|"
            linhas.append(linha)

    except Exception as e:
        print(f"❌ Erro ao exportar NFM: {e}")
    finally:
        session.close()

    return linhas