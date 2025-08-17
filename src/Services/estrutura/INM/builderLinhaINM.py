from src.Utils.fsFormat import format_decimal, format_inteiro

def criarLinhaINM(registro):
    linha = [
        "INM",
        format_decimal(registro.valor),                  # 2 - Valor da Operação
        registro.uf or "",                               # 3 - Unidade da Federação
        registro.cfop or "",                             # 4 - CFOP
        registro.cfop_transferencia or "",               # 5 - CFOP Transferência
        format_decimal(registro.bc_icms),                # 6 - Base de Cálculo do ICMS
        format_decimal(registro.aliq_icms, 4),           # 7 - Alíquota do ICMS
        format_decimal(registro.vl_icms),                # 8 - Valor do ICMS
        format_decimal(registro.isentas_icms),           # 9 - Isentas do ICMS
        format_decimal(registro.outras_icms),            # 10 - Outras do ICMS
        format_decimal(registro.bc_ipi),                 # 11 - Base de Cálculo do IPI
        format_decimal(registro.vl_ipi),                 # 12 - Valor do IPI
        format_decimal(registro.isentas_ipi),            # 13 - Isentas do IPI
        format_decimal(registro.outras_ipi),             # 14 - Outras do IPI
        registro.subst_icms or "",                       # 15
        registro.subst_ipi or "",                        # 16
        registro.subst_cofins or "",                     # 17
        registro.subst_pis or "",                        # 18
        registro.csta or "",                             # 19
        registro.cstb or "",                             # 20
        registro.csosn or "",                            # 21
        registro.csosn_icms or "",                       # 22
        registro.cst_ipi or "",                          # 23
        registro.cofins_monofasico or "",                # 24
        registro.pis_monofasico or "",                   # 25
        registro.calcula_fecop or "",                    # 26
        registro.aliq_decreto_29560 or "",               # 27
        format_decimal(registro.bc_fcp_normal),          # 28
        format_decimal(registro.aliq_fcp_normal),        # 29
        format_decimal(registro.vl_fcp_normal),          # 30
        format_decimal(registro.bc_fcp_st),              # 31
        format_decimal(registro.aliq_fcp_st),            # 32
        format_decimal(registro.vl_fcp_st),              # 33
        format_decimal(registro.aliq_icms_dif),          # 34
    ]

    return "|".join(linha) + "|"
