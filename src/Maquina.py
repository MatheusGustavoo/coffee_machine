from src.Estados import Estado_Maquina


class Maquina:
    _estado: Estado_Maquina | None = None
    _credito: float | None = None

    def __init__(self):
        self._estado = Estado_Maquina.PRONTA
        self._credito = 0.0
