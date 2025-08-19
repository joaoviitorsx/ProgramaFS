import os
from src.Services.parse.parseService import processarLinha
from src.Config.Database.db import SessionLocal

def processarSped(empresa_id: int, periodo: str, caminho: str):
    with SessionLocal() as db:
        for lote in leitor(file_path=caminho):
            print(f"Processando lote com {len(lote)} linhas para empresa {empresa_id} e período {periodo}")

            for linha in lote:
                try:
                    processarLinha(linha, empresa_id, periodo)
                except Exception as e:
                    print(f"⚠️ Erro ao processar linha: {e}")

        db.commit()

def leitor(file_path, encoding='latin1', lote=10000):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    
    with open(file_path, 'r', encoding=encoding) as file:
        lote_buffer = []
        for linha in file:
            linha = linha.rstrip('\n')
            if linha:
                lote_buffer.append(linha)
            
            if len(lote_buffer) >= lote:
                yield lote_buffer
                lote_buffer = []
        
        if lote_buffer:
            yield lote_buffer
