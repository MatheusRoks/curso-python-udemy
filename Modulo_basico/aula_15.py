import os

''' limpeza do terminal'''
def clear_terminal():
    os.system('cls' if os.name == 'ntr' else 'clear')

resto = 0
while True:
    number = input('digite um número inteiro: ')
    if number.isdigit():
        number = int(number)
        resto = number%2
        if resto == 0:
            print(f'O número {number} é par')
            break
        else:
            print(f'O numero {number} é impar')
            break
    else:
        print('digite apenas números inteiros')
        clear_terminal()