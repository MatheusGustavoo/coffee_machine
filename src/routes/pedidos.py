from fastapi import APIRouter

pedidos_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@pedidos_router.post("/")
async def criar_pedido():
    return

@pedidos_router.get("/{id}")
async def obter_pedido(id: int):
    return

@pedidos_router.post("/{id}/cancelar")
async def cancelar_pedido(id: int):
    return


