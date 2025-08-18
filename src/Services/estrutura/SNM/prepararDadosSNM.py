from src.Models.c100Model import RegistroC100
from src.Config.Database.db import SessionLocal
from src.Utils.registroValidacao import parseDecimal

def prepararDadosSNM(empresa_id: int, periodo: str) -> list[dict]:
    session = SessionLocal()
    dados = []

    try:
        notas = session.query(RegistroC100).filter_by(
            empresa_id=empresa_id,
            periodo=periodo,
            ind_oper="1",
            ind_emit="1",
            ativo=True
        ).all()

        base_total = sum(parseDecimal(n.vl_doc) for n in notas)

        if base_total > 0:
            faixa = "1"
            aliquota_efetiva = "1.54"

            dados.append({
                "faixa": faixa,
                "base": base_total,
                "receita_isenta": "",  # não utilizada
                "receita_tributada": base_total,
                "aliquota": aliquota_efetiva,
                "credito": "",  # não utilizado
                "compensacao": "",  # não utilizado
                "indicador_icms": "N",  # fixo
                "indicador_fecop": "N"  # fixo
            })

    except Exception as e:
        print(f"Erro ao preparar dados SNM: {e}")
    finally:
        session.close()

    return dados
