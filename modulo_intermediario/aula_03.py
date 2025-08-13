def par_impar(numero):
    if numero % 2 == 0:
        return "par"
    return "ímpar"

def multiplicacao(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    p_ou_i = par_impar(resultado)
    print(f"O resultado da multiplicação é {resultado}, que é um número {p_ou_i}.")

numeros = [2, 4, 6, 8, 33]
multiplicacao(*numeros)
