class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar(self):
        print(f'{self.nome}, bem-vindo ao programa!')


p1 = Pessoa('Matheus', 'Roks')
print(p1.nome)
print(p1.sobrenome)
print(p1.__dict__)
p1.falar()


# caso usemos o __dict__ vamos ver o dicionário contendo todo o estado do objeto.
# porem, ele possui a propriedade de permitir a alteração ou adição de novos atributos.
