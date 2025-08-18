from src.Services.estrutura.CAB.prepararDadosCAB import prepararDadosCAB
from src.Services.estrutura.CAB.builderLinhaCAB import criarLinhaCAB

def exportarCAB(empresa_id: int, periodo: str) -> list[str]:
    linhas = []

    try:
        dados = prepararDadosCAB(empresa_id, periodo)
        campos = criarLinhaCAB(dados)
        linha = "|" + "|".join(campos) + "|"
        linhas.append(linha)

    except Exception as e:
        print(f"❌ Erro ao exportar CAB: {e}")

    return linhas
