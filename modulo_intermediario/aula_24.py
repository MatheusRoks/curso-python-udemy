def soma(x, y):
    return x + y


def multi(x, y):
    return x * y


def criar_função(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


soma_por_cinco = criar_função(soma, 5)
multiplica_5 = criar_função(multi, 5)
print(soma_por_cinco(2))
print(multiplica_5(10))
