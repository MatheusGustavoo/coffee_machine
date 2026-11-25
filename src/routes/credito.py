from fastapi import APIRouter

credito_router = APIRouter(prefix="/credito", tags=["credito"])

@credito_router.post("/")
async def inserir_credito():
    return