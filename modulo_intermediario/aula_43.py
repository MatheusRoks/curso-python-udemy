class Carrinho:
    def __init__(self):
        self._produtos = []

    def inserir_produtos(self, *produtos):
        self._produtos.extend(produtos)

    def total(self):
        print(sum([p.preco for p in self._produtos]))

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()


class Produtos:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()

p1, p2 = Produtos('caneta', 1.20), Produtos('Mantinha', 30.00)

carrinho.inserir_produtos(p1, p2)
carrinho.total()
carrinho.listar_produtos()
