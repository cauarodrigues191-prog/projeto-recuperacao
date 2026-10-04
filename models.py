from sqlalchemy import Column, Integer, String, Float, Boolean, Date
from database import Base


class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    categoria = Column(String(50), nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable=False, default=0)
    data_validade = Column(Date, nullable=True)
    ativo = Column(Boolean, default=True)
