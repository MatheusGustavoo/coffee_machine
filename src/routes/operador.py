from fastapi import APIRouter

operador_router = APIRouter(prefix="/operador", tags=["operador"])

@operador_router.post("/login")
async def autenticar_operador():
    return

@operador_router.get("/estoque")
async def mostrar_estoque():
    return

@operador_router.post("/estoque/reabastecer")
async def repor_ingrediente():
    return

@operador_router.put("/produtos/{id}/preco")
async def alterar_preco(id: int):
    return

@operador_router.post("/manutencao")
async def modo_manutencao():
    return

@operador_router.post("/limpeza")
async def registrar_limpeza():
    return

@operador_router.get("/relatorio")
async def gerar_relatorio():
    return