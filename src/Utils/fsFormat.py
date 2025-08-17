def fmt_dec(valor, casas=2):
    return f"{valor:.{casas}f}".replace('.', ',') if valor is not None else ""

def fmt_str(valor):
    return str(valor) if valor else ""

def fmt_int(valor):
    return str(int(valor)) if valor else ""