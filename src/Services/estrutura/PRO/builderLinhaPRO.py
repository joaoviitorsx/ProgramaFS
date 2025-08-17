from src.Utils.fsFormat import fmt_str, fmt_dec

def criarLinhaPRO(r):
    return [
        "PRO",                              # 1 - Tipo de registro
        fmt_str(r.cod_item),               # 2 - Código do produto
        fmt_str(r.descr_item),             # 3 - Descrição
        fmt_str(r.cod_barra or ""),        # 4 - Código utilizado estab.
        fmt_str(r.cod_ncm or ""),          # 5 - NCM
        fmt_str(r.unid_inv or ""),         # 6 - Unidade padrão
        "", "",                            # 7-8 Unidades DIEF/CIENF
        "",                                # 9 - Classificação fiscal
        "", "", "",                        # 10-12 - Grupo, gênero, cod. barras
        "",                                # 13 - Redução
        "",                                # 14 - Código GAM57
        "", "", "", "",                    # 15-18 - CSTs
        "",                                # 19 - Código ANP
        "", "",                            # 20-21 - CST Simples, CSOSN
        "", "",                            # 22-23 - Produto Específico, Tipo Medicamento
        fmt_str(r.descr_item),             # 24 - Nome genérico (usando descr_item)
        "N",                                # 25 - Desativado
        "",                                # 26 - Indicador Previdência
        "", "", "", "",                    # 27-30 - NVE, PRODEPE, TIPI, DIEF-PA
        "", "", "", "", "", "", "", "",    # 31-38 - Incentivo, Receita, Aliq etc.
        "", "", "", "", "",                # 39-43 - CEST, Custo, Subst
        "", "", "", "", "", "", "", "",    # 44-51 - Substituições, Tributações
        "", "", "", "",                    # 52-55 - Retenções e decretos
    ]