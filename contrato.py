# aqui fica todas as regras de validação dos dados

from datetime import datetime
from typing import Tuple
from enum import Enum

from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt


class ProdutoEnum(str, Enum):
    produto1 =  "ZapFlow com Gemini"
    produto2 =  "ZapFlow com chatGPT"
    produto3 =  "ZapFlow com Llama3.0"


# docstrings


class Vendas(BaseModel):

    """
    Modelo de dados para as vendas.

    Args:
        email (EmailStr): email do comprador
        data (datetime): data da compra
        valor (PositiveFloat): valor da compra
        produto (PositiveInt): nome do produto
        quantidade (PositiveInt): quantidade de produtos
        produto (ProdutoEnum): categoria do produto
    """
    email: EmailStr # biblioteca do pydantic que valida o email
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum
