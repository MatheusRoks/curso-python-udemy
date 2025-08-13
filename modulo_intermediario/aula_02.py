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


mas caso você passe para a sua função uma tupla como arguento, o *args irá 
empacotar essa tupla dentro de outra tupla, veja:

'''

def soma(*args):
    print(args)

soma(1, 2, 3, 4, 5)  # (1, 2, 3, 4, 5)
soma((1, 2, 3, 4, 5))  # ((1, 2, 3, 4, 5),)

'''
note que no segundo caso, o resultado é uma tupla dentro de outra tupla.
isso porque o *args empacota os argumentos passados para a função em uma tupla.
para desempacotar uma tupla e passar seus valores como argumentos individuais,
basta usar o * na chamada da função:

enquanto isso, a função nativa sum já faz isso internamente, ou seja, ela já desempacota a tupla passada como argumento.
'''