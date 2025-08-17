from src.Models._0000Model import Registro0000
from src.Models.empresaModel import Empresa
from src.Config.Database.db import SessionLocal
from src.Services.estrutura.CAB.builderLinhaCAB import criarLinhaCAB

def exportarCAB(empresa_id: int, periodo: str) -> list[str]:
    session = SessionLocal()
    linhas = []

    try:
        registro = session.query(Registro0000).filter_by(empresa_id=empresa_id, periodo=periodo, ativo=True).first()
        empresa = session.query(Empresa).filter_by(id=empresa_id).first()

        if not registro or not empresa:
            print("❌ Registro 0000 ou Empresa não encontrados.")
            return []

        campos = criarLinhaCAB(
            nome_empresa=empresa.razao_social,
            dt_ini=registro.dt_ini,
            dt_fin=registro.dt_fin,
        )
        linha = "|" + "|".join(campos) + "|"
        linhas.append(linha)

    except Exception as e:
        print(f"Erro ao exportar CAB: {e}")
    finally:
        session.close()

    return linhas