import aiohttp
import asyncio
from src.Utils.cache import cache
from src.Utils.validadores import removedorCaracteres

@cache()
async def buscarInformacoes(cnpj: str) -> tuple[str, str, str, bool, bool]:
    cnpj = removedorCaracteres(cnpj.strip())
    if len(cnpj) != 14:
        raise ValueError("CNPJ inválido: deve conter 14 dígitos")

    url = f'https://minhareceita.org/{cnpj}'
    timeout = aiohttp.ClientTimeout(total=10)
    connector = aiohttp.TCPConnector(ttl_dns_cache=300)

    async with aiohttp.ClientSession(timeout=timeout, connector=connector) as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    dados = await response.json()
                    razao_social = dados.get('razao_social', '').strip()
                    cnae_codigo = str(dados.get('cnae_fiscal', '')).strip()
                    uf = dados.get('uf', '').strip().upper()
                    simples = bool(dados.get('opcao_pelo_simples', False))

                    if not all([razao_social, cnae_codigo, uf]):
                        raise ValueError("Dados incompletos retornados da API")

                    decreto = (uf == "CE" and cnae_codigo)

                    return razao_social, cnae_codigo, uf, simples, decreto
                else:
                    print(f"[API Error] Código de status: {response.status}")
        except asyncio.TimeoutError:
            print("[Error] Timeout da API.")
        except aiohttp.ClientError as e:
            print(f"[Error] Erro HTTP: {e}")
        except Exception as e:
            print(f"[Error] Erro geral: {e}")

    return None, None, None, None, None

async def buscarInformacoesApi(cnpj: str) -> tuple | None:
    try:
        return await buscarInformacoes(cnpj)
    except Exception as e:
        print(f"[Error] Erro ao consultar CNPJ: {e}")
        return None

async def processarCnpjs(lista_cnpjs: list[str]) -> dict[str, tuple]:
    tarefas = [buscarInformacoes(cnpj) for cnpj in lista_cnpjs]
    resultados = await asyncio.gather(*tarefas)
    return dict(zip(lista_cnpjs, resultados))
