from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./estoque.db"

# check_same_thread=False: o SQLite por padrão só aceita uso na thread que criou a conexão
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Fábrica de sessões (cada requisição usa uma sessão própria)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base de todos os models
Base = declarative_base()


def get_db():
    """Dependência: abre uma sessão e garante que ela seja fechada ao final."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
