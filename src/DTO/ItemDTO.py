from pydantic import BaseModel


class ItemDTO(BaseModel):
    nome_item: str
    quantidade_acucar: int
