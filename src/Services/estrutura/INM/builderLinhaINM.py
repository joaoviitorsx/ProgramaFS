from src.Utils.fsFormat import fmt_dec, fmt_str

def criarLinhaINM(dados: dict) -> list[str]:
    return [
        "INM",
        fmt_dec(dados["vl_bc_icms"]),        # 2 - Base de cálculo ICMS
        fmt_str(dados["uf"]),                # 3 - UF
        fmt_str(dados["cfop"]),              # 4 - CFOP
        "", "", "", "", "", "",              # 5–9 - CFOP Transf, Outras bases
        fmt_dec(dados["vl_icms"]),           # 10 - Valor ICMS
        *[""] * 4,                            # 11–14 - IPI e derivados
        dados["indicador_desonerado"],       # 15 - Desoneração
        dados["indicador_fecop"],            # 16 - FECOP
        dados["indicador_antecipado"],       # 17 - Antecipado
        dados["indicador_substituicao"],     # 18 - Substituição
        fmt_str(dados["cst_a"]),             # 19 - CST A
        fmt_str(dados["cst_b"]),             # 20 - CST B
        *[""] * 14                            # 21–34 - Campos extras (vazios)
    ]
