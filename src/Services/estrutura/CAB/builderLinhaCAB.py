from src.Utils.fsFormat import fmt_str

def criarLinhaCAB(dados: dict) -> list[str]:
    return [
        "CAB",                                     # 1 - Tipo de registro
        fmt_str(dados["codigo_empresa_fortes"]),   # 2 - Código da empresa no Fortes
        fmt_str(dados["usuario"]),                 # 3 - Usuário ou sistema gerador
        fmt_str(dados["data_geracao"]),            # 4 - Data de geração (AAAAMMDD)
        fmt_str(dados["nome_empresa"][:60]),       # 5 - Nome da empresa
        fmt_str(dados["data_inicio"]),             # 6 - Data inicial do período
        fmt_str(dados["data_fim"]),                # 7 - Data final do período
        fmt_str(dados["descricao_arquivo"][:40]),  # 8 - Comentário / descrição
        fmt_str(dados["situacao"]),                # 9 - Situação (S = ativo)
    ]
