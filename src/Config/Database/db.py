import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

def carregarVariaveis():
    user = os.getenv('USER')
    password = os.getenv('PASSWORD')
    host = os.getenv('HOST')
    db = os.getenv('DATABASE')
    port = int(os.getenv('PORT'))

    return user, password, host, db, port

def conexao(user='root', password='', host='localhost', db='nome_do_banco', port='PORT'):
    url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8mb4"
    print(f"Conectando ao banco de dados: {url}")
    engine = create_engine(url, echo=True)
    return engine

def getSessao(engine):
    Session = sessionmaker(bind=engine)
    return Session()