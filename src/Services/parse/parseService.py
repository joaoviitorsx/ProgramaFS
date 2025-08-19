from src.Services.registros import registro0000,registro0150,registro0200,registroC100,registroC170,registroC190

DISPATCHER = {
    "0000": registro0000.processar0000,
    "0150": registro0150.processar0150,
    "0200": registro0200.processar0200,
    "C100": registroC100.processarC100,
    "C170": registroC170.processarC170,
    "C190": registroC190.processarC190,
}

def processarLinha(linha: str, empresa_id: int, periodo: str):
    if not linha or linha.strip() == "":
        return

    campos = linha.strip().split("|")

    if len(campos) < 2:
        return

    reg = campos[1].upper()

    funcao_parser = DISPATCHER.get(reg)
    if funcao_parser:
        try:
            funcao_parser(campos, empresa_id, periodo)
        except Exception as e:
            print(f"Erro ao processar registro {reg}: {e}")