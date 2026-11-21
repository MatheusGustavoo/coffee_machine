from pydantic import BaseModel

from src.ItemDTO import ItemDTO


class PedidoDTO(BaseModel):
    itens: list[ItemDTO]
