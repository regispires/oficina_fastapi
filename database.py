from sqlmodel import create_engine, Session, SQLModel
from dotenv import load_dotenv
import os
import logging

# Configurar o logger
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

# Carregar variáveis do arquivo .env
load_dotenv()

# Configuração do banco de dados
engine = create_engine(os.getenv("DATABASE_URL"))

# Criar a(s) tabela(s) no banco de dados
SQLModel.metadata.create_all(engine)

# Inicializa o banco de dados
def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)

def get_session() -> Session:
    return Session(engine)
