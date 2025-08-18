from src.Models._0200Model import Registro0200
from src.Config.Database.db import SessionLocal

# Dicionário auxiliar com descrições conhecidas
DESCRICOES_PADRAO = {
    "UN": "UNIDADE",
    "UN1": "UNIDADE",
    "KG": "QUILOGRAMA",
    "CX": "CAIXA",
    "CX6": "CAIXA COM 6",
    "BD": "BANDEJA",
    "BAN": "BANDEJA",
    "BDJ": "BANDEJA",
    "BDJ0": "BANDEJA 1",
    "DZ": "DUZIA",
    "SC": "SACO",
    "L": "LITRO",
    "LT": "LATA",
    "PC": "PEÇA",
    "PCT": "PACOTE",
    "RL": "ROLO",
    "FD": "FARDO",
    "FR": "FRASCO",
    "CJ": "CONJUNTO"
}

def prepararDadosUND(empresa_id: int, periodo: str) -> list[dict]:
    session = SessionLocal()
    unidades = []

    try:
        results = session.query(Registro0200.unid_inv).filter_by(
            empresa_id=empresa_id,
            periodo=periodo
        ).distinct().all()

        for (sigla,) in results:
            if not sigla:
                continue

            descricao = DESCRICOES_PADRAO.get(sigla.upper(), sigla.upper())
            unidades.append({
                "sigla": sigla.upper(),
                "descricao": descricao
            })

    except Exception as e:
        print(f"❌ Erro ao preparar dados UND: {e}")
    finally:
        session.close()

    return unidades
