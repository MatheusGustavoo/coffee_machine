from enum import Enum


class TipoPedido(Enum):
    EM_PREPARO = "EM_PREPARO"
    PRONTO = "PRONTO"
    CANCELADO = "CANCELADO"
