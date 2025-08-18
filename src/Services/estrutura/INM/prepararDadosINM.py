from src.Utils.registroValidacao import parseDecimal

def preparar_dados_inm(c190, uf_destino: str) -> dict:
    vl_bc_icms = parseDecimal(c190.vl_bc_icms)
    vl_icms = parseDecimal(c190.vl_icms)
    cfop = c190.cfop or ""
    cst = c190.cst or "00"  # Padrão se ausente

    return {
        "vl_bc_icms": vl_bc_icms,
        "uf": uf_destino,
        "cfop": cfop,
        "vl_icms": vl_icms,
        "indicador_desonerado": "N",
        "indicador_fecop": "N",
        "indicador_antecipado": "N",
        "indicador_substituicao": "N",
        "cst_a": cst,
        "cst_b": cst,
    }
