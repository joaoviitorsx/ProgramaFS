from src.Utils.fsFormat import fmt_str

def criarLinhaPRO(r):
    return [
        "PRO",                               # 1 - Tipo de registro
        fmt_str(r.cod_item),                # 2 - Código do produto
        fmt_str(r.descr_item),              # 3 - Descrição
        fmt_str(r.cod_item),                # 4 - Referência (pode repetir cod_item)
        fmt_str(r.cod_ncm or ""),           # 5 - NCM
        fmt_str(r.unid_inv or ""),          # 6 - Unidade padrão
        "", "",                             # 7-8 - Unidades DIEF / CIENF
        "",                                 # 9 - Classificação fiscal
        fmt_str(r.tipo_item or ""),         # 10 - Tipo do produto
        "", "",                             # 11-12 - Grupo, Gênero
        "",                                 # 13 - Código de Barras
        "",                                 # 14 - Código GAM57
        "", "", "", "",                     # 15-18 - CST ICMS, CST IPI, Origem, Tipo
        fmt_str("73"),                      # 19 - CST Simples Nacional (ex: "73")
        fmt_str("73"),                      # 20 - CST COFINS (ex: "73")
        "", "",                             # 21-22 - Substituição, Código ANP
        "", "",                             # 23-24 - Produto Esp., Medicamento
        fmt_str(r.descr_item),              # 25 - Nome genérico
        "N",                                # 26 - Produto desativado (N = ativo)
        "", "", "", "", "", "", "", "",     # 27-34 - Previdência, PRODEPE, etc.
        "", "", "", "", "", "",             # 35-40
        "N",                                # 41 - Tem substituição tributária?
        *[""] * 23,                         # 42–64 - vazios
        "N",                                # 65 - PRODEPE (N padrão)
        *[""] * 4,                          # 66–69
        "N", "N", "N", "N", "N", "N",       # 70–75 - Indicadores fixos
        *[""] * 8,                          # 76–83
        "N"                                 # 84 - Último campo fixo "N"
    ]
