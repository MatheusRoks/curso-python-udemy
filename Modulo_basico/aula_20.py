from clear import clear_terminal
import time

#variáveis
number_one: 0
number_two: 0
oparation = ''
result = 0
check = False

while check!= True:
    print('Irei realizar a operação entre dois numeros que você desejar')
    number_one = input('Digite o primeiro número: ')
    if number_one.isnumeric():
        number_one = float(number_one)
    else:
        print('Valor inválido, favor digitar apenas números')
        time.sleep(2)
        clear_terminal()
        continue
    number_two = input('Digite o segundo número: ')
    if number_two.isnumeric():
        number_two = float(number_two)
        clear_terminal()
    else:
        print('Valor inválido, favor digitar apenas números')
        time.sleep(2)
        clear_terminal()
        continue
    print("""
    Segue abaixo a lista de operadores:
    * = multiplicação
    /  = divisão
    // = divisão inteira
    ** = exponenciação
    -  = subtração
    +  = soma
    """)
    oparation = input("Digite uma operação que deseja realizar: ")
    if number_two == 0 and oparation in ['/', '//']:
        print('Não é possivel realizar divisão por 0, ' \
        'por isso o programa será encerrado')
        time.sleep(2)
        clear_terminal()
        print('programa encerrado')
        break
    match oparation:
        case "*":
            result = number_one * number_two
            clear_terminal()
            print(f'{number_one} * {number_two} = {result}')
        case "-":
            result = number_one - number_two
            clear_terminal()
            print(f'{number_one} - {number_two} = {result}')
        case "+":
            result = number_one + number_two
            clear_terminal()
            print(f'{number_one} + {number_two} = {result}')
        case "/":
            result = number_one / number_two
            clear_terminal()
            print(f'{number_one} / {number_two} = {result}')
        case "**":
            result = number_one ** number_two
            clear_terminal()
            print(f'{number_one} ** {number_two} = {result}')
        case "//":
            result = number_one // number_two
            clear_terminal()
            print(f'{number_one} // {number_two} = {result}')
        case _:
            print('Você não digitou uma operação válida, por questão de \
                  segurança estarei encerrando o programa')
            time.sleep(2)
            clear_terminal()
            print('Programa encerrado')
            break

    mark = input("Deseja continuar fazendo operações? [s]im ou [n]ão: ").lower()
    if mark in ['s', 'sim']:
        check = False
        clear_terminal()
    elif mark in ['n', 'não', 'não', 'no', 'noa']:
        check = True
        clear_terminal()
        print('Programa encerrado')
    else:
        print("Você digitou algo inválido, por segurança estarei encerrando o \
              programa")
        time.sleep(2)
        clear_terminal()
        print('Programa encerrado')
