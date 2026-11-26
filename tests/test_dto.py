import pytest
from pydantic import ValidationError

from src.DTO.ItemDTO import ItemDTO
from src.DTO.PedidoDTO import PedidoDTO


def test_criar_dto_de_pedido_com_itens_validos() -> None:
    pedido = PedidoDTO(
        itens=[
            ItemDTO(nome_item="Cappuccino", quantidade_acucar=2),
            ItemDTO(nome_item="Café expresso", quantidade_acucar=0),
        ]
    )

    assert len(pedido.itens) == 2
    assert pedido.itens[0].nome_item == "Cappuccino"


def test_dto_rejeita_item_sem_campos_obrigatorios() -> None:
    with pytest.raises(ValidationError):
        ItemDTO.model_validate({"nome_item": "Cappuccino"})


def test_dto_pedido_rejeita_item_malformado() -> None:
    with pytest.raises(ValidationError):
        PedidoDTO.model_validate({"itens": [{"nome_item": "Cappuccino"}]})
