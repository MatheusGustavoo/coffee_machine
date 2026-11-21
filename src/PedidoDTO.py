from Bebida import Bebida
from ItemInterface import ItemInterface
from pydantic import BaseModel
from src.ItemDTO import ItemDTO


class PedidoDTO(BaseModel):
    itens: list[ItemDTO]

    def para_pedido(self) -> list[Bebida]:
        itens = []
        for item_dto in self.itens:
            item = ItemInterface.ItemInterface()
            item.set_quantidade(item_dto.quantidade_acucar)
            itens.append(item)
        return itens
