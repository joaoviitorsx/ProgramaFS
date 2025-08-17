from src.Utils.fsFormat import fmt_str, fmt_dec

def criarLinhaPNM(r):
    return [
        "PNM",                        # 1 - Tipo de Registro
        fmt_str(r.cod_item),         # 2 - Produto
        fmt_str(r.cfop),             # 3 - CFOP
        "",                          # 4 - CFOP Transferência
        fmt_str(r.cst_icms),         # 5 - CSTA
        fmt_str(r.cst_icms),         # 6 - CSTB
        fmt_str(r.unid),             # 7 - Unidade de medida
        fmt_dec(r.qtd),              # 8 - Quantidade
        fmt_dec(r.vl_item),          # 9 - Valor Bruto
        "",                          # 10 - Valor IPI
        fmt_str(r.ind_apur or "3"),  # 11 - Tributação ICMS
        *[""] * 19,                  # 12 a 30 - ICMS ST e similares
        fmt_str(r.cst_pis),          # 31 - CST PIS
        fmt_str(r.cst_cofins),       # 32 - CST COFINS
        *[""] * 6,                   # 33 a 38 - Bases e alíquotas PIS/COFINS
        fmt_dec(r.vl_item),          # 39 - Valor Total
        *[""] * 9,                   # 40 a 48 - Natureza Receita etc.
        "1",                         # 49 - Tipo cálculo PIS
        *[""] * 3,                   # 50 a 52
        "1",                         # 53 - Tipo cálculo COFINS
        *[""] * 6,                   # 54 a 59
        fmt_str(r.cod_enq or (r.chv_nfe[:11] if r.chv_nfe else "")),  # 60 - Código ajuste fiscal
        "0",                         # 61 - Compõe valor total da nota
        *[""] * (124 - 62),          # 62 a 124 - campos restantes vazios
    ]