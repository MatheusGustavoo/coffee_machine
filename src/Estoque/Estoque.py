from Estoque.ProdutoEstoque import ProdutoEstoque


class Estoque:
    def __init__(self):
        self._lista_produtos: dict[str, ProdutoEstoque] = {
            produto.NOME: produto()
            for produto in ProdutoEstoque.obter_produtos_disponiveis()
        }

    def listar_produtos(self) -> dict[str, ProdutoEstoque]:
        return self._lista_produtos.copy()

    def decrementar_quantidade(self, nome_produto: str, quantidade: int):
        if nome_produto in self._lista_produtos:
            produto = self._lista_produtos[nome_produto]
            produto.consumir(quantidade)
        else:
            raise KeyError(f"Produto {nome_produto} não encontrado no estoque.")

    def reabastecer_produto(self, nome_produto: str, quantidade: int | None = None):
        if nome_produto in self._lista_produtos:
            produto = self._lista_produtos[nome_produto]
            produto.reabastecer(quantidade)
        else:
            raise KeyError(f"Produto {nome_produto} não encontrado no estoque.")
