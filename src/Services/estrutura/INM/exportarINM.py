from src.Config.Database.db import SessionLocal
from src.Models.c190Model import RegistroC190
from src.Models.empresaModel import EmpresaModel
from src.Services.estrutura.INM.builderLinhaINM import criarLinhaINM
from src.Services.estrutura.INM.prepararDadosINM import preparar_dados_inm

def exportarINM(empresa_id: int, periodo: str) -> list[str]:
    session = SessionLocal()
    linhas = []

    try:
        empresa = session.query(EmpresaModel).filter_by(id=empresa_id).first()
        uf_empresa = empresa.uf if empresa else ""

        registros = session.query(RegistroC190).filter_by(
            empresa_id=empresa_id,
            periodo=periodo,
            ativo=True
        ).all()

        for r in registros:
            dados = preparar_dados_inm(r, uf_empresa)
            campos = criarLinhaINM(dados)
            linha = "|" + "|".join(campos) + "|"
            linhas.append(linha)

    except Exception as e:
        print(f"❌ Erro ao exportar INM: {e}")
    finally:
        session.close()

    return linhas
