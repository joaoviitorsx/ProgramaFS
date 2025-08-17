from src.Models.c170Model import RegistroC170
from src.Config.Database.db import SessionLocal
from Utils.registroValidacao import parseDecimal

#|C170|24|00000000007026||5,00000|UN24|666,00|2,00|0|060|1403|||||0||0|||||||||||||||||||||

def processarC170(campos):
    if len(campos) < 44:
        print(f"⚠️ Linha REG C170 malformada: {campos}")
        return

    db = SessionLocal()
    try:
        registro = RegistroC170(
            reg=campos[1],
            num_item=campos[2],
            cod_item=campos[3],
            descr_compl=campos[4],
            qtd=parseDecimal(campos[5]),
            unid=campos[6],
            vl_item=parseDecimal(campos[7]),
            vl_desc=parseDecimal(campos[8]),
            ind_mov=campos[9],
            cst_icms=campos[10],
            cfop=campos[11],
            cod_nat=campos[12],
            vl_bc_icms=parseDecimal(campos[13]),
            aliq_icms=parseDecimal(campos[14]),
            vl_icms=parseDecimal(campos[15]),
            vl_bc_icms_st=parseDecimal(campos[16]),
            aliq_st=parseDecimal(campos[17]),
            vl_icms_st=parseDecimal(campos[18]),
            ind_apur=campos[19],
            cst_ipi=campos[20],
            cod_enq=campos[21],
            vl_bc_ipi=parseDecimal(campos[22]),
            aliq_ipi=parseDecimal(campos[23]),
            vl_ipi=parseDecimal(campos[24]),
            cst_pis=campos[25],
            vl_bc_pis=parseDecimal(campos[26]),
            aliq_pis=parseDecimal(campos[27]),
            quant_bc_pis=parseDecimal(campos[28]),
            aliq_pis_reais=parseDecimal(campos[29]),
            vl_pis=parseDecimal(campos[30]),
            cst_cofins=campos[31],
            vl_bc_cofins=parseDecimal(campos[32]),
            aliq_cofins=parseDecimal(campos[33]),
            quant_bc_cofins=parseDecimal(campos[34]),
            aliq_cofins_reais=parseDecimal(campos[35]),
            vl_cofins=parseDecimal(campos[36]),
            cod_cta=campos[37],
            vl_abat_nt=parseDecimal(campos[38]),
            c100_id=None,
            filial=None,
            ind_oper=campos[39],
            cod_part=campos[40],
            num_doc=campos[41],
            chv_nfe=campos[42],
            ncm=campos[43] if campos[43] else "",
            mercado="",
            aliquota="",
            resultado="",
            periodo=None,
            empresa_id=None,
            ativo=True
        )
        db.add(registro)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"❌ Erro ao inserir REG C170: {e}")
    finally:
        db.close()