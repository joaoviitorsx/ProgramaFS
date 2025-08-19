from datetime import date
from src.Config.Database.db import SessionLocal
from src.Models.empresaModel import Empresa

def prepararDadosCAB(empresa_id: int, periodo: str) -> dict:
    session = SessionLocal()
    dados = {}

    try:
        empresa = session.query(Empresa).filter_by(id=empresa_id).first()

        if not empresa:
            raise ValueError(f"Empresa ID {empresa_id} não encontrada.")

        ano = periodo[:4]
        mes = periodo[4:]

        dados = {
            "codigo_empresa_fortes": str(empresa.id),  # ou mapeamento específico se necessário
            "usuario": "ACFiscal",                     # ou nome do sistema
            "data_geracao": date.today().strftime("%Y%m%d"),
            "nome_empresa": empresa.razao_social[:60],  # Limita a 60 caracteres
            "data_inicio": f"{ano}{mes}01",
            "data_fim": f"{ano}{mes}30",  # ou calcular corretamente o último dia do mês
            "descricao_arquivo": f"ENTRADAS {empresa.razao_social[:30]} {mes}{ano}",  # Ajustável
            "situacao": "S"
        }

    except Exception as e:
        print(f"❌ Erro ao preparar dados CAB: {e}")
    finally:
        session.close()

    return dados
