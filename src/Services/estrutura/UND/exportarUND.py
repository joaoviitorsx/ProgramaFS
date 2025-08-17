from src.Models.c170Model import RegistroC170
from src.Models._0200Model import Registro0200
from src.Config.Database.db import SessionLocal
from src.Services.estrutura.UND.builderLinhaUND import criarLinhaUND

DESCRICOES_PADRAO = {
    "UN": "UNIDADE",
    "KG": "QUILOGRAMA",
    "LT": "LITRO",
    "PC": "PEÇA",
    "CX": "CAIXA",
    "MT": "METRO",
    "G":  "GRAMAS",
}

def exportarUND(empresa_id: int, periodo: str) -> list[str]:
    session = SessionLocal()
    linhas = []

    try:
        unidades_c170 = session.query(RegistroC170.unid).filter_by(
            empresa_id=empresa_id, periodo=periodo
        ).distinct().all()

        unidades_0200 = session.query(Registro0200.unid_inv).filter_by(
            empresa_id=empresa_id, periodo=periodo
        ).distinct().all()

        unidades = set([u[0] for u in unidades_c170 if u[0]] + [u[0] for u in unidades_0200 if u[0]])

        for unid in unidades:
            descricao = DESCRICOES_PADRAO.get(unid.upper(), f"{unid.upper()} - PADRÃO")
            campos = criarLinhaUND(unid, descricao)
            linha = "|" + "|".join(campos) + "|"
            linhas.append(linha)

    except Exception as e:
        print(f"❌ Erro ao exportar UND: {e}")
    finally:
        session.close()

    return linhas