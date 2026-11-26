from pydantic import BaseModel

from src.DTO.ItemDTO import ItemDTO


class PedidoDTO(BaseModel):
    itens: list[ItemDTO]
