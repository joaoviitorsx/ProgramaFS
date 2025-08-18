from src.Utils.fsFormat import fmt_str, fmt_dec

def criarLinhaNFM(dados: dict) -> list[str]:
    return [
        "NFM",                               # 1
        fmt_str(dados["cod_part"]),         # 2 - Código participante
        fmt_str(dados["operacao"]),         # 3 - E/S
        fmt_str(dados["especie"]),          # 4 - Espécie documento
        fmt_str(dados["tipo_doc"]),         # 5 - Tipo doc (S/N)
        "", "", "",                         # 6-8 - AIDF, série, subsérie
        fmt_str(dados["numero"]),           # 9 - Número NF
        "", "",                             # 10-11 - Formulário inicial/final
        dados["data_emissao"],              # 12 - Data emissão (YYYYMMDD)
        "0",                                # 13 - Situação
        dados["data_entrada"],              # 14 - Data entrada (YYYYMMDD)
        fmt_str(dados["cnpj"]),             # 15 - CNPJ
        "", "", "", "", "", "", "", "",     # 16–23 - GNRE, prot., banco etc.
        fmt_dec(dados["vl_merc"]),          # 24 - Valor produtos
        "", "", "", "", "",                 # 25–29 - Frete, seguros, outros
        "",                                 # 30 - ICMS importado
        "", "",                             # 31–32 - ICMS diferido, IPI
        "", "",                             # 33–34 - ICMS ST, ISS
        "",                                 # 35 - Valor desconto
        fmt_dec(dados["vl_doc"]),           # 36 - Valor total
        "",                                 # 37 - Qtde itens
        "", "", "", "", "", "", "",         # 38–44 - ST, antec., base subst, etc.
        "", "", "",                         # 45–47 - Retenções ISS/serviço
        "", "", "",                         # 48–50 - Frete, tipo fatura, EEC
        "", "", "", "", "", "", "", "",     # 51–58 - base COFINS, PIS, IRPJ, etc.
        "", "", "", "",                     # 59–62 - Retenções
        "",                                 # 63 - Gera transf
        fmt_str(dados["obs_fiscal"]),       # 64 - Observações fiscais
        "",                                 # 65 - Aliq subst
        fmt_str(dados["chave_nfe"]),        # 66 - Chave NF-e
        "", "",                             # 67–68 - INSS, base não cumulativo
        "", "", "",                         # 69–71 - Motivo cancelamento, natureza, código info
        "",                                 # 72 - Info complementar
        "",                                 # 73 - Hora saída
        "", "", "",                         # 74–76 - UF embarque, local, cod contábil
        "",                                 # 77 - NF-e referenciada
        "",                                 # 78 - Info adicional
        fmt_str(dados["indicador_consum_final"]),  # 79 - Indicador consumidor
        "",                                 # 80 - Presença comp
        "",                                 # 81 - Dt contingência
        "",                                 # 82 - Hora contingência
        "", "", "", "", "", "",             # 83–88 - Reconhece NF-e, prestador, etc.
        "", "", "",                         # 89–91 - FCP, NF terceiro
    ]
