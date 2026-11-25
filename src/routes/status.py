from fastapi import APIRouter

status_router = APIRouter(prefix="/status", tags=["status"])

@status_router.get("/")
async def mostrar_status():
    return