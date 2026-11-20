from enum import Enum


class Valores(Enum):
    CINQUENTA_CENTAVOS = 0.50
    UM_REAL = 1.00
    DOIS_REAIS = 2.00
    CINCO_REAIS = 5.00
    DEZ_REAIS = 10.00
    VINTE_REAIS = 20.00

    @classmethod
    def de_valor(cls, valor: float | int) -> "Valores":
        if isinstance(valor, bool) or not isinstance(valor, (float, int)):
            raise TypeError("O valor do crédito deve ser numérico")

        try:
            return cls(valor)
        except ValueError as erro:
            raise ValueError(
                f"Valor de crédito não permitido: {valor:.2f}"
            ) from erro


class Credito:
    MAXIMO = 50.00
    MINIMO = 0.00

    def __init__(self):
        self._atual = 0.00

    @property
    def disponivel(self):
        return self._atual

    def inserir_valor(self, valor: Valores):
        if not isinstance(valor, Valores):
            raise TypeError("Valor inválido")

        if self._atual + valor.value > self.MAXIMO:
            raise ValueError("Limite de crédito excedido")

        self._atual += valor.value

    def zerar(self):
        self._atual = 0.00

    def retirar_valor(self, valor: Valores):
        if not isinstance(valor, Valores):
            raise TypeError("Valor inválido")

        if self._atual - valor.value < 0:
            raise ValueError("Crédito insuficiente")

        self._atual -= valor.value
