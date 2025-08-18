from src.Utils.fsFormat import fmt_str, fmt_dec

def criarLinhaSNM(dados: dict) -> list[str]:
    return [
        "SNM",
        fmt_str(dados["faixa"]),              # 1 - Faixa
        fmt_dec(dados["base"]),               # 2 - Base total
        fmt_dec(dados["receita_isenta"]),     # 3 - Receita isenta (vazio)
        fmt_dec(dados["receita_tributada"]),  # 4 - Receita tributada
        fmt_dec(dados["aliquota"]),           # 5 - Alíquota efetiva
        fmt_dec(dados["credito"]),            # 6 - Crédito
        fmt_dec(dados["compensacao"]),        # 7 - Compensação
        fmt_str(dados["indicador_icms"]),     # 8 - Indicador ICMS
        fmt_str(dados["indicador_fecop"])     # 9 - Indicador FECOP
    ]
