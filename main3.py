from fastapi import FastAPI, Depends
from datetime import datetime
from sqlmodel import SQLModel, Field, select, Session
from contextlib import asynccontextmanager
from database import create_db_and_tables, get_session

# Definição do modelo para Post
class Post(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    titulo: str
    corpo: str
    data: datetime = Field(default_factory=datetime.now)

# Configurações de inicialização
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI()

@app.get("/")
def home():
    return {"msg": "Olá, mundo!"}

@app.post("/posts", response_model=Post)
def criar_post(post: Post, session: Session = Depends(get_session)) -> Post:
    session.add(post)
    session.commit()
    session.refresh(post)
    return post

@app.get("/posts", response_model=list[Post])
def listar_posts(session: Session = Depends(get_session)) -> list[Post]:
    posts = session.exec(select(Post)).all()
    return posts