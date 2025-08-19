from src.Services.leitor.spedReaderService import processarSped
from typing import List

def inserirDadosSped(empresa_id: int, periodo: str, arquivos: List[str]) -> dict:
    try:
        if not arquivos:
            return {"success": False, "mensagem": "Nenhum arquivo informado."}

        for caminho_arquivo in arquivos:
            processarSped(empresa_id, periodo, caminho_arquivo)

        return {
            "success": True,
            "mensagem": f"✅ Arquivos SPED processados com sucesso."
        }

    except Exception as e:
        return {
            "success": False,
            "mensagem": f"❌ Erro ao processar arquivos SPED: {str(e)}"
        }