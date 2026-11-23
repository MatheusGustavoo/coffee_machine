from enum import Enum


class TipoPedido(Enum):
    EM_PREPARO = "Em preparo"
    PRONTO = "Pronto para retirada"
    CANCELADO = "Cancelado"
