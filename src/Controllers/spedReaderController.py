from src.Services.leitor.spedReaderService import leitor
from typing import List

def inserirDadosSped(empresa_id: int, periodo: str, arquivos: List[str]) -> dict:
    try:
        if not arquivos:
            return {"success": False, "mensagem": "Nenhum arquivo informado."}

        for caminho_arquivo in arquivos:
            leitor(empresa_id=empresa_id, periodo=periodo, caminho=caminho_arquivo)

        return {
            "success": True,
            "mensagem": f"✅ Arquivos SPED processados com sucesso."
        }

    except Exception as e:
        return {
            "success": False,
            "mensagem": f"❌ Erro ao processar arquivos SPED: {str(e)}"
        }
