from fastapi import FastAPI
from database import engine, Base
from routers import produtos

# Cria as tabelas no SQLite caso ainda não existam
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Estoque de Alimentos")
app.include_router(produtos.router)
