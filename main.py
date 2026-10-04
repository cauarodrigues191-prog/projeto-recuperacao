from fastapi import FastAPI

from database import Base, engine
from routers.produtos import router as produtos_router


def criar_tabelas():
    """Cria as tabelas do banco de dados caso ainda não existam."""
    Base.metadata.create_all(bind=engine)


criar_tabelas()

app = FastAPI(
    title="API de Gestão de Estoque",
    description="API para gerenciamento de produtos em estoque.",
    version="1.0.0"
)

app.include_router(produtos_router)