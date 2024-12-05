from fastapi import APIRouter
from fastapi import HTTPException, Depends
from sqlmodel import Session, select
from models import Post, Comentario
from database import get_session

router = APIRouter(
    prefix="/posts",  # Prefixo para todas as rotas
    tags=["Posts"],   # Tag para documentação automática
)

@router.post("/", response_model=Post)
def criar_post(post: Post, session: Session = Depends(get_session)) -> Post:
    session.add(post)
    session.commit()
    session.refresh(post)
    return post

@router.get("/", response_model=list[Post])
def listar_posts(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)) -> list[Post]:
    posts = session.exec(select(Post).offset(skip).limit(limit)).all()
    return posts

@router.get("/{post_id}", response_model=Post)
def obter_post(post_id: int, session: Session = Depends(get_session)) -> Post:
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post não encontrado.")
    return post

@router.put("/{post_id}", response_model=Post)
def atualizar_post(post_id: int, post_atualizado: Post, session: Session = Depends(get_session)) -> Post:
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post não encontrado.")
    for key, value in post_atualizado.dict(exclude_unset=True).items():
        setattr(post, key, value)
    session.add(post)
    session.commit()
    session.refresh(post)
    return post

@router.delete("/{post_id}", response_model=dict)
def deletar_post(post_id: int, session: Session = Depends(get_session)) -> dict:
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post não encontrado.")
    session.delete(post)
    session.commit()
    return {"message": "Post deletado com sucesso."}

# Rotas para Comentários
@router.post("/{post_id}/comentarios/", response_model=Comentario)
def criar_comentario(post_id: int, comentario: Comentario, session: Session = Depends(get_session)) -> Comentario:
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post não encontrado.")
    comentario.post_id = post_id
    session.add(comentario)
    session.commit()
    session.refresh(comentario)
    return comentario

@router.get("/{post_id}/comentarios/", response_model=list[Comentario])
def listar_comentarios(post_id: int, session: Session = Depends(get_session)) -> list[Comentario]:
    comentarios = session.exec(select(Comentario).where(Comentario.post_id == post_id)).all()
    return comentarios
