from datetime import datetime
from sqlmodel import SQLModel, Field

# Definição do modelo para Comentário
class Comentario(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    texto: str
    data: datetime = Field(default_factory=datetime.now)
    post_id: int = Field(foreign_key="post.id")

# Definição do modelo para Post
class Post(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    titulo: str
    corpo: str
    data: datetime = Field(default_factory=datetime.now)
