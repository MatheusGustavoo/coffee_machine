from abc import ABC

from src.TipoMedida import TipoMedida


class Item(ABC):
    CAPACIDADE_MAXIMA: int
    LIMITE_ALERTA: int
    medida: TipoMedida

    def __init__(self):
        capacidade = getattr(self, "CAPACIDADE_MAXIMA", self.CAPACIDADE_MAXIMA)
        self.quantidade = capacidade
        self.alerta = "Nível baixo" if self.quantidade < self.LIMITE_ALERTA else ""

    @property
    def capacidade_maxima(self) -> int:
        return self.CAPACIDADE_MAXIMA

    @property
    def limite_alerta(self) -> int:
        return self.LIMITE_ALERTA

    def get_quantidade(self) -> int:
        return self.quantidade

    def set_quantidade(self, quantidade: int) -> None:
        if quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        if quantidade > self.CAPACIDADE_MAXIMA:
            raise ValueError("A quantidade não pode exceder a capacidade máxima.")
        self.quantidade = quantidade

    def consumir(self, quantidade: int) -> None:
        if quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        if quantidade > self.quantidade:
            raise ValueError("Quantidade insuficiente em estoque.")
        self.quantidade -= quantidade

    def reabastecer(self, quantidade: int | None = None) -> None:
        if quantidade is None:
            self.quantidade = self.CAPACIDADE_MAXIMA
        else:
            if quantidade < 0:
                raise ValueError("A quantidade não pode ser negativa.")
            self.quantidade = min(self.quantidade + quantidade, self.CAPACIDADE_MAXIMA)
