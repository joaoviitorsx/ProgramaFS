import os
import importlib

def gerarArquivo(empresa_id: int, periodo: str, output_path: str) -> str:
    modulos = ['CAB', 'PAR', 'UND', 'PRO', 'NFM', 'PNM', 'SNM', 'INM']
    
    linhas = []
    for modulo in modulos:
        exportador = importlib.import_module(f'src.Services.estrutura.{modulo}.exportar{modulo}')
        linhas.extend(getattr(exportador, f'exportar{modulo}')(empresa_id, periodo))

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(linhas))

    return output_path