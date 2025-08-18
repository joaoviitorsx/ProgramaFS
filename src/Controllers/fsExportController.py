import os
from src.Services.estrutura.fsExportService import gerarArquivo

def exportarFS(empresa_id: int, periodo: str, nome_empresa: str) -> dict:
    try:
        nome_arquivo = f"{nome_empresa.upper()}_{periodo}.fs".replace(" ", "_")
        output_path = os.path.join("output", "fs", nome_arquivo)

        caminho_final = gerarArquivo(empresa_id, periodo, output_path)

        return {
            "success": True,
            "mensagem": f"✅ Arquivo gerado com sucesso: {caminho_final}",
            "caminho": caminho_final
        }

    except Exception as e:
        return {
            "success": False,
            "mensagem": f"❌ Erro ao gerar arquivo FS: {str(e)}",
            "caminho": None
        }
