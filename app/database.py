import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Substitua 'usuario', 'senha' e 'nome_do_banco' pelos seus dados locais
# Exemplo: "postgresql://postgres:admin123@localhost/bookstore_db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@db:5432/bookstore_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependência que as rotas usarão para abrir/fechar a conexão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()