from datetime import date
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class ProdutoBase(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100)
    categoria: str = Field(..., min_length=2, max_length=50)
    preco: float = Field(..., gt=0)
    quantidade: int = Field(..., ge=0)
    data_validade: Optional[date] = None
    ativo: bool = True


class ProdutoCreate(ProdutoBase):
    """Entrada para POST e PUT (PUT atualiza todos os campos)."""
    pass


class ProdutoResponse(ProdutoBase):
    id: int

    # Permite converter o objeto SQLAlchemy em schema Pydantic
    model_config = ConfigDict(from_attributes=True)
