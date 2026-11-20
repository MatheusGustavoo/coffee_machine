from Maquina import Estado_Maquina


class Pedido:
    _valor_total: float
    _status_maquina: Estado_Maquina

    def __init__(self, status_maquina: Estado_Maquina) -> None:
        self._valor_total = 0.0
        self._status_maquina = status_maquina

    def incluir_item():
        pass

    def remover_item():
        pass

    def get_valor_total(self) -> float:
        return self._valor_total

    def _update_valor_total(self, valor: float, operacao: str) -> None:
        if operacao == "adicionar":
            self._valor_total += valor
        elif operacao == "subtrair":
            self._valor_total -= valor
