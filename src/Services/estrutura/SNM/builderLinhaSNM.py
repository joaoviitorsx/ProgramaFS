from src.Utils.fsFormat import fmt_str, fmt_dec

def criarLinhaSNM(r):
    return [
        "SNM",                       # 1 - Tipo Registro
        fmt_str(r.tipo),            # 2 - Tipo de substituição
        fmt_dec(r.custo),           # 3 - Custo de aquisição
        fmt_dec(r.agr),             # 4 - Percentual de agregação
        fmt_dec(r.base_calc),       # 5 - Base de cálculo
        fmt_dec(r.aliquota),        # 6 - Alíquota interna
        fmt_dec(r.credito),         # 7 - Crédito de origem
        fmt_dec(r.recolhido),       # 8 - Valor já recolhido
        fmt_str(r.calcula_fecop)    # 9 - S/N para cálculo de Fecop
    ]