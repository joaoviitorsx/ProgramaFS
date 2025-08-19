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
    port = os.getenv('PORT')

    return user, password, host, db, port

def conexao(user='root', password='', host='localhost', db='nome_do_banco', port=3306):
    url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8mb4"
    print(f"Conectando ao banco de dados: {url}")
    engine = create_engine(url, echo=False)
    return engine

user, password, host, db, port = carregarVariaveis()
engine = conexao(user, password, host, db, port)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def getSessao():
    return SessionLocal()

def getDb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()