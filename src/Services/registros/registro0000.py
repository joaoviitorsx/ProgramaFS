from src.Models._0000Model import Registro0000
from src.Config.Database.db import SessionLocal
from Utils.registroValidacao import parseData

#|0000|019|0|01072025|31072025|JM SUPERMERCADO COMERCIO DE ALIMENTOS LTDA|00092104000173||CE|068913290|2304251|||B|1|

def processar0000(campos):
    if len(campos) < 16:
        print(f"⚠️ Linha REG 0000 malformada: {campos}")
        return

    db = SessionLocal()
    try:
        registro = Registro0000(
            reg=campos[1],
            cod_ver=campos[2],
            cod_fin=campos[3],
            dt_ini=parseData(campos[4]),
            dt_fin=parseData(campos[5]),
            nome=campos[6],
            cnpj=campos[7],
            cpf=campos[8],
            uf=campos[9],
            ie=campos[10],
            cod_num=campos[11],
            im=campos[12],
            suframa=campos[13],
            ind_perfil=campos[14],
            ind_ativ=campos[15],
            filial=None,
            periodo=None,
            ativo=True
        )
        db.add(registro)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Erro ao inserir REG 0000: {e}")
    finally:
        db.close()
