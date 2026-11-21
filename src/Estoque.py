from src.ProdutoEstoque import Item


class Estoque:
    _lista_produtos: list[Item]

    def __init__(self):
        self._lista_produtos = []

    def adicionar_produto(self, produto):
        self._lista_produtos.append(produto)

    def remover_produto(self, produto):
        if produto in self._lista_produtos:
            self._lista_produtos.remove(produto)

    def listar_produtos(self):
        return self._lista_produtos

    def vazio(self):
        return len(self._lista_produtos) == 0
