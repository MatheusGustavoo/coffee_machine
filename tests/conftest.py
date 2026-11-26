import importlib

import pytest

from src.Estoque.Estoque import Estoque


@pytest.fixture(scope="session")
def inventory_products_registered() -> None:
    for module in (
        "src.Estoque.Acucar",
        "src.Estoque.Agua",
        "src.Estoque.CafeEmGraos",
        "src.Estoque.ChocolateEmPo",
        "src.Estoque.Copos",
        "src.Estoque.Leite",
    ):
        importlib.import_module(module)


@pytest.fixture
def estoque(inventory_products_registered: None) -> Estoque:
    return Estoque()
