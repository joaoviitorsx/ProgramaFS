from src.Utils.fsFormat import fmt_str

def criarLinhaPAR(r):
    return [
        "PAR",                              # 1 - Tipo Registro
        fmt_str(r.cod_part),               # 2 - Código do participante
        fmt_str(r.nome),                   # 3 - Nome
        fmt_str(r.uf),                     # 4 - UF
        fmt_str(r.cnpj or r.cpf),          # 5 - CNPJ/CPF
        fmt_str(r.ie),                     # 6 - IE
        "",                                # 7 - Inscrição Municipal
        "", "", "", "", "",                # 8-12 - Indicadores fiscais
        "N",                               # 13 - Livro eletrônico
        "N",                               # 14 - Produtor primário
        "35",                              # 15 - Tipo logradouro (exemplo genérico)
        fmt_str(r.ende),                   # 16 - Logradouro
        fmt_str(r.num),                    # 17 - Número
        fmt_str(r.compl),                  # 18 - Complemento
        "1",                               # 19 - Tipo Bairro
        fmt_str(r.bairro),                 # 20 - Bairro
        fmt_str(r.cod_mun or ""),          # 21 - Código IBGE município
        "",                                # 22 - CEP
        "", "",                            # 23-24 - DDD, Telefone
        fmt_str(r.suframa),                # 25 - Suframa
        "", "",                            # 26-27 - Subst ISS, Conta Fiscal
        "1058",                            # 28 - Código país (Brasil)
        "N",                               # 29 - Participação Exterior
        "1",                               # 30 - Indicador de participação ICMS
        "",                                # 31 - E-mail
        "N",                               # 32 - Indicador hospital público
        "N",                               # 33 - Indicador hospital privado
        "", "",                            # 34-35 - CNAE, código contábil
        "N",                               # 36 - Produtor Rural
        "0",                               # 37 - Indicativo de aquisição
        "N",                               # 38 - Substituição tributária
        "", "", "", "",                    # 39–42 - Reservados
    ]
