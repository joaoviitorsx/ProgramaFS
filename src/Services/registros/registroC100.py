from src.Models.c100Model import RegistroC100
from src.Config.Database.db import SessionLocal
from Utils.registroValidacao import parseData, parseDecimal

#|C100|1|0||65|00|2|000009087|23250700092104000173650020000090871022312201|23072025|23072025|10,90|0|||10,90|9||||0|0||||||||

def processarC100(campos):
    if len(campos) < 30:
        print(f"⚠️ Linha REG C100 malformada: {campos}")
        return

    db = SessionLocal()
    try:
        registro = RegistroC100(
            reg=campos[1],
            ind_oper=campos[2],
            ind_emit=campos[3],
            cod_part=campos[4],
            cod_mod=campos[5],
            cod_sit=campos[6],
            ser=campos[7],
            num_doc=campos[8],
            chv_nfe=campos[9],
            dt_doc=parseData(campos[10]),
            dt_e_s=parseData(campos[11]),
            vl_doc=parseDecimal(campos[12]),
            ind_pgto=campos[13],
            vl_desc=parseDecimal(campos[14]),
            vl_abat_nt=parseDecimal(campos[15]),
            vl_merc=parseDecimal(campos[16]),
            ind_frt=campos[17],
            vl_frt=parseDecimal(campos[18]),
            vl_seg=parseDecimal(campos[19]),
            vl_out_da=parseDecimal(campos[20]),
            vl_bc_icms=parseDecimal(campos[21]),
            vl_icms=parseDecimal(campos[22]),
            vl_bc_icms_st=parseDecimal(campos[23]),
            vl_icms_st=parseDecimal(campos[24]),
            vl_ipi=parseDecimal(campos[25]),
            vl_pis=parseDecimal(campos[26]),
            vl_cofins=parseDecimal(campos[27]),
            vl_pis_st=parseDecimal(campos[28]),
            vl_cofins_st=parseDecimal(campos[29]),
            ativo=True
        )
        db.add(registro)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"❌ Erro ao inserir REG C100: {e}")
    finally:
        db.close()