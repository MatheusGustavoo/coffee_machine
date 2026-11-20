class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        if produto in self.produtos:
            self.produtos.remove(produto)

    def listar_produtos(self):
        return self.produtos

    def vazio(self):
        return len(self.produtos) == 0
