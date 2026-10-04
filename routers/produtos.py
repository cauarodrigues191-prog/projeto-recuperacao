from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models import Produto
from schemas import ProdutoCreate, ProdutoResponse


router = APIRouter(prefix="/produtos", tags=["Produtos"])


@router.post(
    "",
    response_model=ProdutoResponse,
    status_code=status.HTTP_201_CREATED
)
def criar_produto(
    dados: ProdutoCreate,
    db: Session = Depends(get_db)
):
    produto = Produto(**dados.model_dump())

    db.add(produto)
    db.commit()
    db.refresh(produto)

    return produto


@router.get("", response_model=List[ProdutoResponse])
def listar_produtos(
    categoria: Optional[str] = None,
    ativo: Optional[bool] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Produto)

    if categoria:
        query = query.filter(Produto.categoria == categoria)

    if ativo is not None:
        query = query.filter(Produto.ativo == ativo)

    return query.all()


@router.get("/{produto_id}", response_model=ProdutoResponse)
def buscar_produto(
    produto_id: int,
    db: Session = Depends(get_db)
):
    produto = (
        db.query(Produto)
        .filter(Produto.id == produto_id)
        .first()
    )

    if not produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )

    return produto


@router.put("/{produto_id}", response_model=ProdutoResponse)
def atualizar_produto(
    produto_id: int,
    dados: ProdutoCreate,
    db: Session = Depends(get_db)
):
    produto = (
        db.query(Produto)
        .filter(Produto.id == produto_id)
        .first()
    )

    if not produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )

    for campo, valor in dados.model_dump().items():
        setattr(produto, campo, valor)

    db.commit()
    db.refresh(produto)

    return produto


@router.delete("/{produto_id}")
def deletar_produto(
    produto_id: int,
    db: Session = Depends(get_db)
):
    produto = (
        db.query(Produto)
        .filter(Produto.id == produto_id)
        .first()
    )

    if not produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )

    db.delete(produto)
    db.commit()

    return {
        "mensagem": "Produto removido com sucesso"
    }