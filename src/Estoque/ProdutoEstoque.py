from abc import ABC


class ProdutoEstoque(ABC):
    CAPACIDADE_MAXIMA: int
    LIMITE_ALERTA: int
    NOME: str
    _produtos_disponiveis = []

    def __init__(self):
        self.quantidade = self.CAPACIDADE_MAXIMA

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if not getattr(cls, "__abstractmethods__", False) and cls not in ProdutoEstoque._produtos_disponiveis:
            ProdutoEstoque._produtos_disponiveis.append(cls)

    @classmethod
    def obter_produtos_disponiveis(cls):
        return cls._produtos_disponiveis.copy()

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


Item = ProdutoEstoque
