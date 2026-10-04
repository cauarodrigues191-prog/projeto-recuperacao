# API de Gestão de Estoque de Alimentos

API RESTful com FastAPI, Pydantic e SQLAlchemy, persistindo dados em SQLite.

## Como executar

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install "fastapi[standard]" sqlalchemy
fastapi dev main.py
```

Documentação interativa: http://127.0.0.1:8000/docs

## Estrutura

- `database.py`: engine, SessionLocal, Base e get_db
- `models.py`: modelo SQLAlchemy `Produto`
- `schemas.py`: schemas Pydantic de entrada e resposta
- `routers/produtos.py`: CRUD de produtos
- `main.py`: instância do FastAPI, router e `create_all()`

## Contrato das rotas

| Método | Rota | Descrição | Status |
|---|---|---|---|
| POST | /produtos/ | Cadastra produto | 201 |
| GET | /produtos/?categoria=&ativo= | Lista com filtros opcionais | 200 |
| PUT | /produtos/{id} | Atualiza todos os campos | 200 / 404 |
| DELETE | /produtos/{id} | Remove produto | 200 / 404 |
| GET | /produtos/{id} | Busca produto por ID | 200 / 404 |
## Exemplo de corpo (POST/PUT)

```json
{
  "nome": "Arroz 5kg",
  "categoria": "Grãos",
  "preco": 28.9,
  "quantidade": 40,
  "data_validade": "2027-03-01",
  "ativo": true
}
```
## Histórico de desenvolvimento
Projeto desenvolvido passo a passo com FastAPI, Pydantic e SQLAlchemy.