from src.Config.Database.db import SessionLocal
from src.Models.c100Model import RegistroC100
from src.Models.c170Model import RegistroC170
from src.Models._0150Model import Registro0150
from src.Services.estrutura.NFM.builderLinhaNFM import criarLinhaNFM
from src.Services.estrutura.NFM.prepararDadosNFM import preparar_dados_nfm

def exportarNFM(empresa_id: int, periodo: str) -> list[str]:
    session = SessionLocal()
    linhas = []

    try:
        notas = session.query(RegistroC100).filter_by(
            empresa_id=empresa_id,
            periodo=periodo,
            ativo=True
        ).all()

        for c100 in notas:
            c170 = session.query(RegistroC170).filter_by(
                empresa_id=empresa_id,
                periodo=periodo,
                cod_doc=c100.num_doc
            ).first()

            participante = session.query(Registro0150).filter_by(
                empresa_id=empresa_id,
                periodo=periodo,
                cod_part=c100.cod_part
            ).first()

            dados = preparar_dados_nfm(c100, c170, participante)
            campos = criarLinhaNFM(dados)
            linha = "|" + "|".join(campos) + "|"
            linhas.append(linha)

    except Exception as e:
        print(f"❌ Erro ao exportar NFM: {e}")
    finally:
        session.close()

    return linhas
