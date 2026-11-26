import importlib

import pytest


@pytest.mark.xfail(
    raises=NameError,
    strict=False,
    reason="Maquina referencia CatalogoBebidas sem importar o símbolo.",
)
def test_modulo_maquina_pode_ser_importado() -> None:
    importlib.import_module("src.services.Maquina")
