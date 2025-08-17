from src.Utils.fsFormat import fmt_str

def criarLinhaUND(cod_unidade: str, descricao: str):
    return [
        "UND",                        # 1 - Tipo de registro
        fmt_str(cod_unidade[:6]),     # 2 - Unidade de medida
        fmt_str(descricao[:60])       # 3 - Descrição
    ]