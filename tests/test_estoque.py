import pytest

from src.Catalogo.Bebida import Bebida
from src.Estoque.Agua import Agua


def test_estoque_inicia_com_capacidade_total(estoque) -> None:
    produtos = estoque.listar_produtos()

    assert produtos
    assert all(
        produto.get_quantidade() == produto.capacidade_maxima
        for produto in produtos.values()
    )


def test_listar_produtos_nao_expoe_o_dicionario_interno(estoque) -> None:
    produtos = estoque.listar_produtos()
    produtos.clear()

    assert estoque.listar_produtos()


def test_verificar_disponibilidade_e_consumir_ingredientes(estoque) -> None:
    bebida = Bebida(
        nome="Bebida de teste",
        agua=40,
        cafe=8,
        leite=100,
        chocolate=5,
        preco=6.50,
        acucar=10,
        copo=1,
    )

    assert estoque.verificar_disponibilidade_bebida(bebida, 1)

    estoque.decrementar_quantidade(bebida, 1)
    produtos = estoque.listar_produtos()

    assert produtos["agua"].get_quantidade() == 1960
    assert produtos["cafe"].get_quantidade() == 492
    assert produtos["leite"].get_quantidade() == 900
    assert produtos["chocolate"].get_quantidade() == 395
    assert produtos["acucar"].get_quantidade() == 290
    assert produtos["copo"].get_quantidade() == 49


def test_indisponibilidade_quando_quantidade_excede_estoque(estoque) -> None:
    bebida = Bebida(
        nome="Bebida de teste",
        agua=40,
        cafe=8,
        leite=0,
        chocolate=0,
        preco=4.00,
        copo=1,
    )

    assert not estoque.verificar_disponibilidade_bebida(bebida, 51)


def test_decremento_insuficiente_informa_produto(estoque) -> None:
    bebida = Bebida(
        nome="Bebida de teste",
        agua=2001,
        cafe=0,
        leite=0,
        chocolate=0,
        preco=4.00,
        copo=0,
    )

    with pytest.raises(ValueError, match="produto agua"):
        estoque.decrementar_quantidade(bebida, 1)

    assert estoque.listar_produtos()["agua"].get_quantidade() == 2000


def test_reabastecer_retorna_produtos_a_capacidade_maxima(estoque) -> None:
    agua = estoque.listar_produtos()["agua"]
    agua.consumir(100)

    estoque.reabastecer()

    assert agua.get_quantidade() == agua.capacidade_maxima


def test_produto_estoque_valida_quantidades_e_reabastecimento() -> None:
    produto = Agua()
    capacidade = produto.capacidade_maxima
    produto.set_quantidade(5)

    with pytest.raises(ValueError, match="não pode ser negativa"):
        produto.set_quantidade(-1)
    with pytest.raises(ValueError, match="capacidade máxima"):
        produto.set_quantidade(capacidade + 1)
    with pytest.raises(ValueError, match="não pode ser negativa"):
        produto.consumir(-1)
    with pytest.raises(ValueError, match="insuficiente"):
        produto.consumir(6)

    produto.consumir(2)
    produto.reabastecer(10)
    assert produto.get_quantidade() == 13

    produto.reabastecer(capacidade)
    assert produto.get_quantidade() == capacidade

    produto.reabastecer()
    assert produto.get_quantidade() == capacidade
