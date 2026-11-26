import pytest

from src.Catalogo.Bebida import Bebida
from src.Catalogo.CatalogoBebidas import BebidaFactory, CatalogoBebidas


@pytest.fixture
def catalogo() -> CatalogoBebidas:
    bebida = Bebida(
        nome="Café de teste",
        agua=40,
        cafe=8,
        leite=0,
        chocolate=0,
        preco=4.00,
    )
    return CatalogoBebidas({bebida.nome: bebida})


def test_buscar_bebida_ignora_espacos_e_maiusculas(
    catalogo: CatalogoBebidas,
) -> None:
    bebida = catalogo.buscar("  CAFÉ DE TESTE ")

    assert bebida.nome == "Café de teste"


def test_listar_devolve_tupla_com_itens_do_catalogo(
    catalogo: CatalogoBebidas,
) -> None:
    bebidas = catalogo.listar()

    assert isinstance(bebidas, tuple)
    assert [bebida.nome for bebida in bebidas] == ["Café de teste"]


def test_buscar_bebida_inexistente_gera_erro(catalogo: CatalogoBebidas) -> None:
    with pytest.raises(KeyError, match="Bebida não encontrada"):
        catalogo.buscar("chá")


def test_alterar_preco_valido(catalogo: CatalogoBebidas) -> None:
    catalogo.alterar_preco("Café de teste", 5.25)

    assert catalogo.buscar("Café de teste").preco == 5.25


def test_rejeitar_preco_negativo(catalogo: CatalogoBebidas) -> None:
    with pytest.raises(ValueError, match="não pode ser negativo"):
        catalogo.alterar_preco("Café de teste", -1.00)


def test_factory_cria_copia_e_aplica_acucar(catalogo: CatalogoBebidas) -> None:
    bebida_original = catalogo.buscar("Café de teste")
    fabrica = BebidaFactory(catalogo)

    sem_acucar = fabrica.criar("Café de teste")
    com_acucar = fabrica.criar("Café de teste", 2)

    assert sem_acucar is not bebida_original
    assert sem_acucar.acucar == 0
    assert com_acucar.acucar == 2
    assert bebida_original.acucar == 0


def test_factory_rejeita_quantidade_negativa_de_acucar(
    catalogo: CatalogoBebidas,
) -> None:
    fabrica = BebidaFactory(catalogo)

    with pytest.raises(ValueError, match="açúcar não pode ser negativa"):
        fabrica.criar("Café de teste", -1)
