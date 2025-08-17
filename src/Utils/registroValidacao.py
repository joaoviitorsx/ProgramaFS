from datetime import datetime
from decimal import Decimal, InvalidOperation

def parseData(valor: str):
    try:
        if valor and len(valor.strip()) == 8:
            return datetime.strptime(valor.strip(), "%d%m%Y").date()
    except Exception:
        pass
    return None

def parseDecimal(valor: str):
    try:
        if valor:
            return Decimal(valor.strip().replace(',', '.'))
    except (InvalidOperation, AttributeError):
        pass
    return Decimal("0.00")
