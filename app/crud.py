from sqlalchemy.orm import Session
from . import models, schemas

# --- OPERAÇÕES PARA AUTORES ---

def get_autor(db: Session, autor_id: int):
    return db.query(models.Autor).filter(models.Autor.id == autor_id).first()

def get_autores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Autor).offset(skip).limit(limit).all()

def create_autor(db: Session, autor: schemas.AutorCreate):
    db_autor = models.Autor(**autor.dict())
    db.add(db_autor)
    db.commit()
    db.refresh(db_autor)
    return db_autor

def update_autor(db: Session, autor_id: int, autor_data: schemas.AutorCreate):
    db_autor = get_autor(db, autor_id)
    if db_autor:
        for key, value in autor_data.dict().items():
            setattr(db_autor, key, value)
        db.commit()
        db.refresh(db_autor)
    return db_autor

def delete_autor(db: Session, autor_id: int):
    db_autor = get_autor(db, autor_id)
    if db_autor:
        db.delete(db_autor)
        db.commit()
        return True
    return False

# --- OPERAÇÕES PARA LIVROS ---

def get_livros(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Livro).offset(skip).limit(limit).all()

def get_livro(db: Session, livro_id: int):
    return db.query(models.Livro).filter(models.Livro.id == livro_id).first()

def create_livro(db: Session, livro: schemas.LivroCreate):
    db_livro = models.Livro(**livro.dict())
    db.add(db_livro)
    db.commit()
    db.refresh(db_livro)
    return db_livro

def update_livro(db: Session, livro_id: int, livro_data: schemas.LivroCreate):
    db_livro = get_livro(db, livro_id)
    if db_livro:
        for key, value in livro_data.dict().items():
            setattr(db_livro, key, value)
        db.commit()
        db.refresh(db_livro)
    return db_livro

def delete_livro(db: Session, livro_id: int):
    db_livro = get_livro(db, livro_id)
    if db_livro:
        db.delete(db_livro)
        db.commit()
        return True
    return False