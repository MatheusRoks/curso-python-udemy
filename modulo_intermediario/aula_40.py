class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    @classmethod
    def anonimo(cls, idade):
        return cls(f'Anônimo {idade}')

    @classmethod
    def create_with_auth(cls, name, password):
        conection = cls()
        conection.name = name
        conection.password = password
        return conection


p1 = Pessoa('Luiz')
p2 = Pessoa.anonimo(20)
print(p1.nome)
print(p2.nome)
