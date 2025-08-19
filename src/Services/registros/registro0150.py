from src.Models._0150Model import Registro0150
from src.Config.Database.db import SessionLocal

# |0150|3037|SEARA COMERCIO DE ALIMENTOS LTDA|1058|83044016007306|||2301000||RODOVIA BR 116|0|KM 23 SALA 2,|CAMARA|

def processar0150(campos, empresa_id: int, periodo: str):
    if len(campos) < 15:
        print(f"⚠️ Linha REG 0150 malformada: {campos}")
        return

    db = SessionLocal()
    try:
        registro = Registro0150(
            reg=campos[1],
            cod_part=campos[2],
            nome=campos[3],
            cod_pais=campos[4],
            cnpj=campos[5] if campos[5] else None,
            cpf=campos[6] if campos[6] else None,
            ie=campos[7],
            cod_mun=campos[8],
            suframa=campos[9],
            ende=campos[10],
            num=campos[11],
            compl=campos[12],
            bairro=campos[13],
            uf=campos[14],
            empresa_id=empresa_id,
            periodo=periodo,
            ativo=True
        )
        db.add(registro)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"❌ Erro ao inserir REG 0150: {e}")
    finally:
        db.close()
