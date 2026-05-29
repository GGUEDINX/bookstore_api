# BookStore API - Sistema de Gerenciamento de Biblioteca Digital

Esta é uma API RESTful desenvolvida para o gerenciamento de um catálogo de livros e autores, permitindo operações completas de CRUD (Create, Read, Update, Delete) com persistência em banco de dados relacional.

Este projeto faz parte do Trabalho Prático da disciplina de Linguagem de Programação Python.

## Tecnologias Utilizadas

* **Python 3.14+**
* **FastAPI**: Framework web de alta performance.
* **PostgreSQL**: Banco de dados relacional.
* **SQLAlchemy**: ORM para mapeamento objeto-relacional.
* **Pydantic**: Validação de dados e schemas.
* **Docker/Rancher Desktop**: Conteinerização do banco de dados.
* **Uvicorn**: Servidor ASGI para rodar a aplicação.

## Arquitetura do Projeto

O projeto segue uma estrutura modular para facilitar a manutenção e escalabilidade:

```text
bookstore_api/
├── app/
│   ├── __init__.py    # Transforma a pasta em um pacote Python
│   ├── main.py        # Ponto de entrada da API e definição de rotas
│   ├── models.py      # Modelos do Banco de Dados (SQLAlchemy)
│   ├── schemas.py     # Schemas de validação (Pydantic)
│   ├── crud.py        # Lógica de persistência e manipulação de dados
│   └── database.py    # Configuração da conexão com o banco
├── requirements.txt   # Dependências do projeto
└── README.md          # Documentação