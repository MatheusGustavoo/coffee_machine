from dataclasses import asdict

from src.Catalogo.Bebida import Bebida
from src.Estoque.ProdutoEstoque import ProdutoEstoque


class Estoque:
    def __init__(self):
        self._lista_produtos: dict[str, ProdutoEstoque] = {
            produto.NOME: produto()
            for produto in ProdutoEstoque.obter_produtos_disponiveis()
        }

    def listar_produtos(self) -> dict[str, ProdutoEstoque]:
        return self._lista_produtos.copy()

    def decrementar_quantidade(self, bebida: Bebida, quantidade: int):
        for produto in asdict(bebida):
            if produto in self._lista_produtos:
                try:
                    self._lista_produtos[produto].consumir(
                        getattr(bebida, produto) * quantidade
                    )
                except ValueError as e:
                    raise ValueError(
                        f"Erro ao decrementar quantidade do produto {produto}: {e}"
                    )

    def reabastecer(self):
        for produto in self._lista_produtos.values():
            produto.reabastecer()

    def verificar_disponibilidade_bebida(self, bebida: Bebida, quantidade: int) -> bool:
        for produto in asdict(bebida):
            if produto in self._lista_produtos and (
                self._lista_produtos[produto].get_quantidade()
                < getattr(bebida, produto) * quantidade
            ):
                return False
        return True
