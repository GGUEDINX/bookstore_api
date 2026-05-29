from pydantic import BaseModel
from datetime import date
from typing import List, Optional

# --- SCHEMAS PARA LIVROS ---
class LivroBase(BaseModel):
    titulo: str
    ano_publicacao: int
    genero: str

class LivroCreate(LivroBase):
    autor_id: int  # Necessário para vincular ao autor na criação

class Livro(LivroBase):
    id: int
    autor_id: int

    class Config:
        from_attributes = True # Permite que o Pydantic leia modelos do SQLAlchemy

# --- SCHEMAS PARA AUTORES ---
class AutorBase(BaseModel):
    nome: str
    nacionalidade: str
    data_nascimento: date

class AutorCreate(AutorBase):
    pass

class Autor(AutorBase):
    id: int
    livros: List[Livro] = [] # Quando listarmos o autor, os livros dele vêm junto

    class Config:
        from_attributes = True