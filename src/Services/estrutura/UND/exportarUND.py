from src.Services.estrutura.UND.prepararDadosUND import prepararDadosUND
from src.Services.estrutura.UND.builderLinhaUND import criarLinhaUND

def exportarUND(empresa_id: int, periodo: str) -> list[str]:
    linhas = []

    try:
        dados = prepararDadosUND(empresa_id, periodo)

        for d in dados:
            campos = criarLinhaUND(d["sigla"], d["descricao"])
            linha = "|" + "|".join(campos) + "|"
            linhas.append(linha)

    except Exception as e:
        print(f"❌ Erro ao exportar UND: {e}")

    return linhas
