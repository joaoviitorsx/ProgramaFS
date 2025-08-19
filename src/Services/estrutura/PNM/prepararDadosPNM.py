from decimal import Decimal
from src.Utils.registroValidacao import parseDecimal

def prepararDadosPNM(registro_c170):
    produto = str(registro_c170.cod_item).lstrip("0")
    cfop = registro_c170.cfop or ""
    unidade = registro_c170.unid or "UN"
    quantidade = parseDecimal(registro_c170.qtd or "0")
    vl_item = parseDecimal(registro_c170.vl_item or "0")
    vl_desc = parseDecimal(registro_c170.vl_desc or "0")
    vl_total = (vl_item - vl_desc).quantize(Decimal("0.02"))

    aliq_pis = Decimal("1.65")
    aliq_cofins = Decimal("7.60")
    valor_pis = (vl_total * aliq_pis / 100).quantize(Decimal("0.01"))
    valor_cofins = (vl_total * aliq_cofins / 100).quantize(Decimal("0.01"))
    diferenca_arred = (vl_total - vl_item).quantize(Decimal("0.02"))

    cod_ajuste = "31103020302"
    tipo_calc = "1"
    cst_padrao = registro_c170.cst_icms or "50"
    tributacao_icms = "3"

    return {
        "produto": produto,
        "cfop": cfop,
        "cfop_transferencia": "",
        "csta": cst_padrao,
        "cstb": cst_padrao,
        "unidade": unidade,
        "quantidade": quantidade,
        "valor_bruto": vl_item,
        "valor_total": vl_total,
        "base_pis": vl_total,
        "base_cofins": vl_total,
        "aliq_pis": aliq_pis,
        "aliq_cofins": aliq_cofins,
        "valor_pis": valor_pis,
        "valor_cofins": valor_cofins,
        "dif_arred": diferenca_arred,
        "cst_pis": cst_padrao,
        "cst_cofins": cst_padrao,
        "tributacao_icms": tributacao_icms,
        "tipo_calc_pis": tipo_calc,
        "tipo_calc_cofins": tipo_calc,
        "codigo_ajuste": cod_ajuste,
        "comp_valor_total": "0",
        "ressarc_st": "N",
        "prodepe": "N",
        "decreto": "N"
    }
