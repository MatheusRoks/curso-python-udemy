def func():
    def func2():
        print(x)
    print(x)

x = 10

func()
# func2() essa função não irá funcionar, visto que ela está definida dentro de func e não pode ser chamada diretamente fora dela.

'''
def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

com isso podemos entender que o *args é uma forma de passar uma quantidade variável de argumentos para a função.
sendo esses argumentos não nomeados e acessados como uma tupla dentro da função.
isso impede que a nossa função quebre caso a quantidade de argumentos seja diferente do esperado.

claro que o exemplo acima é desnecessário, visto que a função nativa sum já faz isso.
mas serve para exemplificar o uso do *args.

'''