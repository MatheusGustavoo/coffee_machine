import pytest

from src.services.Credito import Credito, Valores


@pytest.mark.parametrize(
    ("valor", "esperado"),
    [
        (0.50, Valores.CINQUENTA_CENTAVOS),
        (1.00, Valores.UM_REAL),
        (2.00, Valores.DOIS_REAIS),
        (5.00, Valores.CINCO_REAIS),
        (10.00, Valores.DEZ_REAIS),
        (20.00, Valores.VINTE_REAIS),
    ],
)
def test_converter_denominacoes_validas(valor: float, esperado: Valores) -> None:
    assert Valores.de_valor(valor) is esperado


@pytest.mark.parametrize("valor", [0.25, 3.00])
def test_rejeitar_denominacao_nao_permitida(valor: float) -> None:
    with pytest.raises(ValueError, match="não permitido"):
        Valores.de_valor(valor)


@pytest.mark.parametrize("valor", [True, "1.00"])
def test_rejeitar_credito_que_nao_seja_numero(valor: object) -> None:
    with pytest.raises(TypeError, match="deve ser numérico"):
        Valores.de_valor(valor)  # type: ignore[arg-type]


def test_inserir_credito_ate_o_limite_e_rejeitar_excesso() -> None:
    credito = Credito()
    credito.inserir_valor(Valores.VINTE_REAIS)
    credito.inserir_valor(Valores.VINTE_REAIS)
    credito.inserir_valor(Valores.DEZ_REAIS)

    assert credito.disponivel == 50.00

    with pytest.raises(ValueError, match="Limite de crédito excedido"):
        credito.inserir_valor(Valores.CINQUENTA_CENTAVOS)

    assert credito.disponivel == 50.00


def test_debitar_e_zerar_credito() -> None:
    credito = Credito()
    credito.inserir_valor(Valores.DEZ_REAIS)
    credito.retirar_valor(Valores.CINCO_REAIS)

    assert credito.disponivel == 5.00

    credito.zerar()

    assert credito.disponivel == 0.00


def test_rejeitar_debito_sem_saldo_suficiente_sem_alterar_saldo() -> None:
    credito = Credito()
    credito.inserir_valor(Valores.CINCO_REAIS)

    with pytest.raises(ValueError, match="Crédito insuficiente"):
        credito.retirar_valor(Valores.DEZ_REAIS)

    assert credito.disponivel == 5.00


def test_debito_exige_valor_da_lista_de_denominacoes() -> None:
    credito = Credito()

    with pytest.raises(TypeError, match="Valor inválido"):
        credito.retirar_valor(2.00)  # type: ignore[arg-type]
