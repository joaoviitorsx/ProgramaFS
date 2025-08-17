from src.Models.c190Model import RegistroC190
from src.Config.Database.db import SessionLocal
from Utils.registroValidacao import parseDecimal

#|C190|060|5405||26,97|0|0|0|0|0|0||1

def processarC190(campos):
    if len(campos) < 15:
        print(f"⚠️ Linha REG C190 malformada: {campos}")
        return

    db = SessionLocal()
    try:
        registro = RegistroC190(
            reg=campos[1],
            cst_icms=campos[2],
            cfop=campos[3],
            aliq_icms=parseDecimal(campos[4]),
            vl_opr=parseDecimal(campos[5]),
            vl_bc_icms=parseDecimal(campos[6]),
            vl_icms=parseDecimal(campos[7]),
            vl_bc_icms_st=parseDecimal(campos[8]),
            vl_icms_st=parseDecimal(campos[9]),
            vl_red_bc=parseDecimal(campos[10]),
            vl_ipi=parseDecimal(campos[11]),
            cod_obs=campos[12],
            empresa_id=None,
            periodo=None,
            c100_id=None,
            ativo=True
        )
        db.add(registro)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"❌ Erro ao inserir REG C190: {e}")
    finally:
        db.close()