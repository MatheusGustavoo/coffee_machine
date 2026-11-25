from fastapi import APIRouter

troco_router = APIRouter(prefix="/troco", tags=["troco"])

@troco_router.post("/")
async def devolver_troco():
    return