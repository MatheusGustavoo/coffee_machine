from src.Estados import Estado_Maquina


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

    # TODO: Implementar a função de verificação de condições para aceitar ou recusar o pedido ao implementar as regras de negócio.
    # def _verificar_condicoes_pedido(self, ) -> bool:
    #     status = (
    #         self._status_maquina == Estado_Maquina.PRONTA
    #         and self.self._valor_total > 0
    #         and self._status_maquina == Estado_Maquina.MANUTENCAO,
    #     )
    #     if self._status_maquina == Estado_Maquina.PRONTA:
    #         return True
    #     else:
    #         return False
