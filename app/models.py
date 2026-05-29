from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from .database import Base

class Autor(Base):
    __tablename__ = "autores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    nacionalidade = Column(String)
    data_nascimento = Column(Date)

    # Relacionamento: um autor tem muitos livros
    # O cascade="all, delete" garante que se apagar o autor, os livros dele sumam também
    livros = relationship("Livro", back_populates="autor", cascade="all, delete")

class Livro(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    ano_publicacao = Column(Integer)
    genero = Column(String)
    autor_id = Column(Integer, ForeignKey("autores.id"))

    # Referência de volta para o autor
    autor = relationship("Autor", back_populates="livros")