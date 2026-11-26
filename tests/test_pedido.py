import pytest

from src.DTO.ItemDTO import ItemDTO
from src.DTO.PedidoDTO import PedidoDTO
from src.services.Pedido import Pedido


@pytest.mark.integration
def test_pedido_consome_estoque_e_calcula_preco(estoque) -> None:
    pedido = Pedido(estoque)
    itens = PedidoDTO(
        itens=[ItemDTO(nome_item="Cappuccino", quantidade_acucar=10)]
    )

    pedido.incluir_item(itens)

    assert pedido.get_valor_total() == 6.50
    produtos = estoque.listar_produtos()
    assert produtos["agua"].get_quantidade() == 1960
    assert produtos["cafe"].get_quantidade() == 492
    assert produtos["leite"].get_quantidade() == 900
    assert produtos["chocolate"].get_quantidade() == 395
    assert produtos["acucar"].get_quantidade() == 290
    assert produtos["copo"].get_quantidade() == 49


def test_pedido_invalido_levanta_erro_sem_consumir_estoque(estoque) -> None:
    pedido = Pedido(estoque)
    itens = PedidoDTO(
        itens=[ItemDTO(nome_item="Bebida inexistente", quantidade_acucar=0)]
    )

    with pytest.raises(ValueError, match="Erro ao incluir item"):
        pedido.incluir_item(itens)

    assert pedido.get_valor_total() == 0.0
    assert estoque.listar_produtos()["agua"].get_quantidade() == 2000
