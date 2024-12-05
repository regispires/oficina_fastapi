from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"msg": "Olá, mundo!"}

@app.get("/posts/{id}")
def read_item(id: int, titulo: str | None = None):
    return {"id": id, "titulo": titulo}
