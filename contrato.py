# aqui fica todas as regras de validação dos dados

from datetime import datetime
from typing import Tuple
from enum import Enum

from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt


class ProdutoEnum(str, Enum):
    produto1 =  "ZapFlow com Gemini"
    produto2 =  "ZapFlow com chatGPT"
    produto3 =  "ZapFlow com Llama3.0"

class Vendas(BaseModel):
    email: EmailStr # biblioteca do pydantic que valida o email
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum
