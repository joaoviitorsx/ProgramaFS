import os

def leitor(file_path, encoding='latin1', lote=10000):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    
    with open(file_path, 'r', encoding=encoding) as file:
        lote = []
        for linha in file:
            linha = linha.rstrip('\n')
            if linha:
                lote.append(linha)
            
            if len(lote) >= lote:
                yield lote
                lote = []
        
        if lote:
            yield lote