from src.Utils.fsFormat import fmt_str, fmt_dec, fmt_data

def criarLinhaNFM(r):
    return [
        "NFM",                        # 1 - Tipo Registro
        fmt_str(r.estabelecimento),  # 2 - Código do Estabelecimento
        fmt_str(r.operacao),         # 3 - E ou S
        fmt_str(r.especie),          # 4 - Espécie (ex: NFE)
        fmt_str(r.doc_proprio),      # 5 - S ou N
        fmt_str(r.aidf or ""),       # 6 - Número AIDF
        fmt_str(r.serie or ""),      # 7 - Série
        fmt_str(r.subserie or ""),   # 8 - Subsérie
        fmt_str(r.numero),           # 9 - Número NF
        fmt_str(r.formulario_ini),   # 10
        fmt_str(r.formulario_fin),   # 11
        fmt_data(r.data_emissao),    # 12
        fmt_str(r.situacao),         # 13 - Situação
        fmt_data(r.data_entrada),    # 14
        fmt_str(r.cod_part),         # 15 - Participante
        fmt_str(r.gnre_vinculada),   # 16
        fmt_str(r.tipo_icms),        # 17
        fmt_str(r.mes_ano),          # 18
        fmt_str(r.protocolo),        # 19
        fmt_data(r.venc_gnre),       # 20
        fmt_data(r.recolhimento_gnre),  # 21
        fmt_str(r.banco_gnre),       # 22
        fmt_str(r.agencia_gnre),     # 23
        fmt_str(r.dv_gnre),          # 24
        fmt_str(r.gnre_autenticada), # 25
        fmt_dec(r.vl_prod),          # 26
        fmt_dec(r.vl_frt),           # 27
        fmt_dec(r.vl_seg),           # 28
        fmt_dec(r.outras_despesas),  # 29
        fmt_dec(r.vl_icms_imp),      # 30
        fmt_str(r.icms_diferido),    # 31
        fmt_dec(r.vl_ipi),           # 32
        fmt_dec(r.vl_icms_st),       # 33
        fmt_dec(r.vl_serv_iss),      # 34
        fmt_dec(r.vl_desc),          # 35
        fmt_dec(r.vl_total),         # 36
        fmt_str(r.qtd_itens),        # 37
        fmt_str(r.subst_recolher),   # 38
        fmt_str(r.antecip_recolher), # 39
        fmt_str(r.difal_recolher),   # 40
        fmt_str(r.subst_base),       # 41
        fmt_dec(r.base_subst),       # 42
        fmt_dec(r.vl_antecip),       # 43
        fmt_str(r.iss_retido),       # 44
        fmt_data(r.dt_ret_iss),      # 45
        fmt_str(r.servico),          # 46
        fmt_data(r.dt_entrada_uf),   # 47
        fmt_str(r.frete_por_conta),  # 48
        fmt_str(r.tipo_fatura),      # 49
        fmt_str(r.eec),              # 50
        fmt_str(r.cupom),            # 51
        fmt_dec(r.base_cofins),      # 52
        fmt_dec(r.base_pis),         # 53
        fmt_dec(r.base_csl1),        # 54
        fmt_dec(r.base_csl2),        # 55
        fmt_dec(r.base_irpj1),       # 56
        fmt_dec(r.base_irpj2),       # 57
        fmt_dec(r.base_irpj3),       # 58
        fmt_dec(r.base_irpj4),       # 59
        fmt_dec(r.ret_cofins),       # 60
        fmt_dec(r.ret_pis),          # 61
        fmt_dec(r.ret_csl),          # 62
        fmt_dec(r.ret_irpj),         # 63
        fmt_str(r.gera_transf),      # 64
        fmt_str(r.obs),              # 65
        fmt_dec(r.aliq_subst),       # 66
        fmt_str(r.chave),            # 67
        fmt_dec(r.inss),             # 68
        fmt_dec(r.base_nao_cumul),   # 69
        fmt_str(r.motivo_canc),      # 70
        fmt_str(r.natureza),         # 71
        fmt_str(r.codigo_info),      # 72
        fmt_str(r.info_complementar),# 73
        fmt_str(r.hora_saida),       # 74
        fmt_str(r.uf_embarque),      # 75
        fmt_str(r.local_embarque),   # 76
        fmt_str(r.cod_contabil),     # 77
        fmt_str(r.nfe_ref),          # 78
        fmt_str(r.info_adicional),   # 79
        fmt_str(r.ind_consumidor),   # 80
        fmt_str(r.presenca_comp),    # 81
        fmt_data(r.dt_contingencia), # 82
        fmt_str(r.hora_contingencia),# 83
        fmt_str(r.reconhece_nfe),    # 84
        fmt_str(r.informada_pelo_contribuinte), # 85
        fmt_dec(r.icms_desonerado),  # 86
        fmt_str(r.prestador_servico),# 87
        fmt_str(r.cno),              # 88
        fmt_data(r.dt_escrituracao), # 89
        fmt_dec(r.fcp_subst),        # 90
        fmt_str(r.nfe_terceiro),     # 91
    ]