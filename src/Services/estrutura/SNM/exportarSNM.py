from src.Services.estrutura.SNM.prepararDadosSNM import prepararDadosSNM
from src.Services.estrutura.SNM.builderLinhaSNM import criarLinhaSNM

def exportarSNM(empresa_id: int, periodo: str) -> list[str]:
    linhas = []

    try:
        dados = prepararDadosSNM(empresa_id, periodo)

        for d in dados:
            campos = criarLinhaSNM(d)
            linha = "|" + "|".join(campos) + "|"
            linhas.append(linha)

    except Exception as e:
        print(f"❌ Erro ao exportar SNM: {e}")

    return linhas
