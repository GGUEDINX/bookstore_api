from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas, database
from .database import engine, get_db

# Cria as tabelas no PostgreSQL automaticamente ao iniciar a API
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="BookStore API - Sistema de Biblioteca Digital")

# --- ENDPOINTS DE AUTORES ---

@app.post("/autores", response_model=schemas.Autor, status_code=status.HTTP_201_CREATED)
def criar_autor(autor: schemas.AutorCreate, db: Session = Depends(get_db)):
    return crud.create_autor(db=db, autor=autor)

@app.get("/autores", response_model=List[schemas.Autor])
def listar_autores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_autores(db, skip=skip, limit=limit)

@app.get("/autores/{autor_id}", response_model=schemas.Autor)
def buscar_autor(autor_id: int, db: Session = Depends(get_db)):
    db_autor = crud.get_autor(db, autor_id=autor_id)
    if db_autor is None:
        raise HTTPException(status_code=404, detail="Autor não encontrado")
    return db_autor

@app.put("/autores/{autor_id}", response_model=schemas.Autor)
def atualizar_autor(autor_id: int, autor: schemas.AutorCreate, db: Session = Depends(get_db)):
    db_autor = crud.update_autor(db, autor_id=autor_id, autor_data=autor)
    if db_autor is None:
        raise HTTPException(status_code=404, detail="Autor não encontrado")
    return db_autor

@app.delete("/autores/{autor_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_autor(autor_id: int, db: Session = Depends(get_db)):
    sucesso = crud.delete_autor(db, autor_id=autor_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Autor não encontrado")
    return None

# --- ENDPOINTS DE LIVROS ---

@app.post("/livros", response_model=schemas.Livro, status_code=status.HTTP_201_CREATED)
def criar_livro(livro: schemas.LivroCreate, db: Session = Depends(get_db)):
    # Valida se o autor existe antes de criar o livro
    db_autor = crud.get_autor(db, autor_id=livro.autor_id)
    if not db_autor:
        raise HTTPException(status_code=400, detail="Autor informado não existe")
    return crud.create_livro(db=db, livro=livro)

@app.get("/livros", response_model=List[schemas.Livro])
def listar_livros(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_livros(db, skip=skip, limit=limit)

@app.get("/livros/{livro_id}", response_model=schemas.Livro)
def buscar_livro(livro_id: int, db: Session = Depends(get_db)):
    db_livro = crud.get_livro(db, livro_id=livro_id)
    if db_livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return db_livro

@app.put("/livros/{livro_id}", response_model=schemas.Livro)
def atualizar_livro(livro_id: int, livro: schemas.LivroCreate, db: Session = Depends(get_db)):
    db_livro = crud.update_livro(db, livro_id=livro_id, livro_data=livro)
    if db_livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return db_livro

@app.delete("/livros/{livro_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_livro(livro_id: int, db: Session = Depends(get_db)):
    sucesso = crud.delete_livro(db, livro_id=livro_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return None