from fastapi import APIRouter
from fastapi import HTTPException, Depends
from sqlmodel import Session
from models import Comentario
from database import get_session

router = APIRouter(
    prefix="/comentarios",  # Prefixo para todas as rotas
    tags=["Comentarios"],   # Tag para documentação automática
)

@router.get("/{comentario_id}", response_model=Comentario)
def obter_comentario(comentario_id: int, session: Session = Depends(get_session)) -> Comentario:
    comentario = session.get(Comentario, comentario_id)
    if not comentario:
        raise HTTPException(status_code=404, detail="Comentário não encontrado.")
    return comentario

@router.delete("/{comentario_id}", response_model=dict)
def deletar_comentario(comentario_id: int, session: Session = Depends(get_session)) -> dict:
    comentario = session.get(Comentario, comentario_id)
    if not comentario:
        raise HTTPException(status_code=404, detail="Comentário não encontrado.")
    session.delete(comentario)
    session.commit()
    return {"message": "Comentário deletado com sucesso."}