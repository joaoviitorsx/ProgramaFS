from src.Utils.fsFormat import fmt_str

def criarLinhaPAR(r):
    return [
        "PAR",                           # 1 - Tipo Registro
        fmt_str(r.cod_part),            # 2 - Código do participante
        fmt_str(r.nome),                # 3 - Nome
        fmt_str(r.uf),                  # 4 - UF
        fmt_str(r.cnpj or r.cpf),       # 5 - CNPJ/CPF
        fmt_str(r.ie),                  # 6 - IE
        "",                             # 7 - IM
        "", "", "", "", "",             # 8-12 - ISS, DIEF, DIC, DEMMS, Órgão Público
        "", "",                         # 13-14 - Livro eletrônico, Produtor primário
        "", "",                         # 15-16 - Simples, Tipo logradouro
        "", "", "", "", "",             # 17-21 - Endereço
        "",                             # 22 - CEP
        fmt_str(r.cod_mun),             # 23 - Código Município (IBGE)
        "", "",                         # 24-25 - DDD, Tel
        fmt_str(r.suframa),             # 26 - Suframa
        "",                             # 27 - Subst. ISS
        "", "",                         # 28-29 - Conta remetente/destinatário
        "1058",                         # 30 - País (fixo: Brasil)
        "N",                            # 31 - Exterior
        "N",                            # 32 - Contribuinte de ICMS
        "", "", "", "", "", "",         # 33-38 - E-mail, hospitais, CNAE etc.
        "", "",                         # 39-40 - Produtor Rural, Indicativo aquisição
    ]