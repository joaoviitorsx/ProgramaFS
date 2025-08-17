from datetime import datetime
from src.Utils.fsFormat import fmt_str, fmt_data

def criarLinhaCAB(nome_empresa: str, dt_ini, dt_fin, comentario: str = "Apuração ICMS", sistema_origem="Sistema ICMS"):
    return [
        "CAB",                              # 1 - Tipo de registro
        "172",                              # 2 - Versão do leiaute Fortes
        fmt_str(sistema_origem),           # 3 - Sistema origem
        fmt_data(datetime.now().date()),   # 4 - Data de geração
        fmt_str(nome_empresa[:15]),        # 5 - Empresa (limite de 15 chars)
        fmt_data(dt_ini),                  # 6 - Data inicial do período
        fmt_data(dt_fin),                  # 7 - Data final do período
        fmt_str(comentario[:40]),          # 8 - Comentário
        "N"                                 # 9 - Alíquotas específicas (N = não utiliza)
    ]