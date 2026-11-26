import asyncio

import pytest
from httpx import ASGITransport, AsyncClient

from main import app


@pytest.mark.integration
def test_listar_produtos_responde_com_status_e_corpo_esperados() -> None:
    async def obter_produtos():
        transporte = ASGITransport(app=app)
        async with AsyncClient(
            transport=transporte,
            base_url="http://test",
        ) as cliente:
            return await cliente.get("/produtos/")

    resposta = asyncio.run(obter_produtos())

    assert resposta.status_code == 200
    assert resposta.json() == {"mensagem": "Rota de produtos funcionando"}
