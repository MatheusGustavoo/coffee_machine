import enum


class Estado_Maquina(enum.Enum):
    PRONTA = "aceita crédito e pedidos"
    AGUARDANDO_LIMPEZA = (
        "atingido o limite de 30 preparos desde a última limpeza; pedidos bloqueados."
    )
    MANUTENCAO = (
        "colocada pelo operador para reabastecer ou limpar; pedidos bloqueados."
    )
    PREPARANDO = "há uma bebida em preparo; novos pedidos são recusados até o término."


class Maquina:
    _estado: Estado_Maquina
    _credito: float

    def __init__(self) -> None:
        self._estado = Estado_Maquina.PRONTA
        self._credito = 0.0
        print(
            f"Máquina inicializada. Estado: {self._estado.value}. Crédito: R${self._credito:.2f}"
        )
