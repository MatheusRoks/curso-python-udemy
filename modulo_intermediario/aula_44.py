class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Enderecos(rua, numero))

    def exibir_listas(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)


class Enderecos:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero


cliente1 = Cliente('Matheus')
cliente1.inserir_endereco('Rua A', 123)
cliente1.inserir_endereco('Rua B', 456)
cliente1.exibir_listas()
