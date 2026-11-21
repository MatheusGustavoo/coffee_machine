from pydantic import BaseModel

from DTO.ItemDTO import ItemDTO


class PedidoDTO(BaseModel):
    itens: list[ItemDTO]
