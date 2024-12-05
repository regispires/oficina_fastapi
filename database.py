from sqlmodel import create_engine, Session, SQLModel
from dotenv import load_dotenv
import os
import logging

# Configurar o logger
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

# Carregar variáveis do arquivo .env
load_dotenv()

# Criar a engine de conexão com o banco de dados
engine = create_engine(os.getenv("DATABASE_URL"))

# Inicializa o banco de dados
def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)

# Retorna uma sessão do banco de dados
def get_session() -> Session:
    return Session(engine)
