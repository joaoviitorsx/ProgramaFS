from src.Models._0200Model import Registro0200
from src.Config.Database.db import SessionLocal
from Utils.registroValidacao import parseDecimal

#|0200|00000000000002|FAR TRIGO D.BENTA C/FERMENTO 1KG|||UN|99|11010010||11|||1704418|

def processar0200(campos):
    if len(campos) < 14:
        print(f"⚠️ Linha REG 0200 malformada: {campos}")
        return

    db = SessionLocal()
    try:
        registro = Registro0200(
            reg=campos[1],
            cod_item=campos[2],
            descr_item=campos[3],
            cod_barra=campos[4] if campos[4] else None,
            cod_ant_item=campos[5] if campos[5] else None,
            unid_inv=campos[6],
            tipo_item=campos[7],
            cod_ncm=campos[8] if campos[8] else None,
            ex_ipi=campos[9] if campos[9] else None,
            cod_gen=campos[10] if campos[10] else None,
            cod_list=campos[11] if campos[11] else None,
            aliq_icms=parseDecimal(campos[12]) if campos[12] else None,
            cest=campos[13] if campos[13] else None,
            ativo=True
        )
        db.add(registro)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"❌ Erro ao inserir REG 0200: {e}")
    finally:
        db.close()