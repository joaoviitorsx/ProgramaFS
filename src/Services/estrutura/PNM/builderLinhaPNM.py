from src.Utils.fsFormat import fmt_str, fmt_dec

def criarLinhaPNM(dados: dict) -> list[str]:
    return [
        "PNM",                              # 1
        fmt_str(dados["produto"]),         # 2
        fmt_str(dados["cfop"]),            # 3
        fmt_str(dados["cfop_transferencia"]),  # 4
        fmt_str(dados["csta"]),            # 5
        fmt_str(dados["cstb"]),            # 6
        fmt_str(dados["unidade"]),         # 7
        fmt_dec(dados["quantidade"]),      # 8
        fmt_dec(dados["valor_bruto"]),     # 9
        "",                                # 10 - Valor IPI
        fmt_str(dados["tributacao_icms"]), # 11
        *[""] * 19,                         # 12 a 30
        fmt_str(dados["cst_pis"]),         # 31
        fmt_str(dados["cst_cofins"]),      # 32
        fmt_dec(dados["base_pis"]),        # 33
        "", "",                             # 34, 35
        fmt_dec(dados["base_cofins"]),     # 36
        "", "",                             # 37, 38
        fmt_dec(dados["valor_total"]),     # 39
        *[""] * 9,                          # 40–48
        fmt_str(dados["tipo_calc_pis"]),   # 49
        fmt_dec(dados["aliq_pis"]),        # 50
        "", "",                             # 51–52
        fmt_str(dados["tipo_calc_cofins"]),# 53
        fmt_dec(dados["aliq_cofins"]),     # 54
        fmt_dec(dados["valor_pis"]),       # 55
        "",                                 # 56
        fmt_dec(dados["valor_cofins"]),    # 57
        "",                                 # 58
        fmt_dec(dados["dif_arred"]),       # 59
        fmt_str(dados["codigo_ajuste"]),   # 60
        fmt_str(dados["comp_valor_total"]),# 61
        *[""] * 34,                         # 62–95
        fmt_str(dados["ressarc_st"]),      # 96
        *[""] * 22,                         # 97–118
        fmt_str(dados["prodepe"]),         # 119
        *[""] * 5,                          # 120–124
        fmt_str(dados["decreto"]),         # 125
        *[""] * 3                           # 126–128
    ]
