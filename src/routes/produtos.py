from fastapi import APIRouter

produtos_router = APIRouter(prefix="/produtos", tags=["produtos"])


@produtos_router.get("/")
async def listar_produtos():
    return {"mensagem": "Rota de produtos funcionando"}
