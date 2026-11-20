from abc import ABC

# class medida(Enum):
#     ML = "ml"
#     UNIDADE = "unidade"
#     G = "g"


# class tipo_item(Enum):
#     AGUA = ("Água", medida.ML)
#     LEITE = ("Leite", medida.ML)
#     CHOCOLATE = ("Chocolate", medida.ML)
#     CAFE = ("Café", medida.ML)
#     ACUCAR = ("Açúcar", medida.G)
#     COPO = ("Copo", medida.UNIDADE)


class ItemInterface(ABC):
    _quantidade: float
    alerta: str

    def get_quantidade(self) -> float:
        return self._quantidade

    def set_quantidade(self, quantidade: float):
        self._quantidade = quantidade

    def get_alerta(self) -> str:
        return self.alerta

    def set_alerta(self, alerta: str):
        self.alerta = alerta
