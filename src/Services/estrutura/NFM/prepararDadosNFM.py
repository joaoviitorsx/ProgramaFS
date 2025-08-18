from src.Utils.registroValidacao import parseDecimal
from datetime import datetime

def formatarData(data_obj):
    return data_obj.strftime("%Y%m%d") if data_obj else ""

def prepararDadosNFM(c100, c170=None, participante=None):
    cod_part = c100.cod_part
    operacao = "E" if c100.ind_oper == "0" else "S"
    especie = c100.cod_mod or "NFE"
    tipo = c100.ind_emit or "S"
    numero = c100.num_doc.zfill(9) if c100.num_doc else ""
    data_emissao = formatarData(c100.dt_doc)
    data_entrada = formatarData(c100.dt_e_s)
    vl_merc = parseDecimal(c100.vl_merc)
    vl_doc = parseDecimal(c100.vl_doc)
    chave = c100.chv_nfe or ""
    cfop = c170.cfop if c170 else ""

    return {
        "cod_part": cod_part,
        "operacao": operacao,
        "especie": especie,
        "tipo_doc": tipo,
        "numero": numero,
        "data_emissao": data_emissao,
        "data_entrada": data_entrada,
        "cnpj": participante.cnpj if participante else "",
        "vl_merc": vl_merc,
        "vl_doc": vl_doc,
        "cfop": cfop,
        "chave_nfe": chave,
        "obs_fiscal": "",  # pode ser implementado depois
        "indicador_st": "N",
        "indicador_icms_deson": "N",
        "indicador_devolucao": "N",
        "indicador_cfe": "N",
        "indicador_consum_final": "N",
        "finalidade_emissao": "R",
        "tipo_operacao": "V",
        "compoe_total": "0"
    }
