import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def checker(number):
    try:
        number = float(number)
        return True
    except ValueError:
        return False

def duplicator(number):
    return float(number) * 2

def triplicator(number):
    return float(number) * 3

def quadruplicator(number):
    return duplicator(number) * 2

def main():
    clear_terminal()
    print("Bem-vindo ao programa de duplicação, triplicação e quadruplicação de números!")
    while True:
        number = input("Digite um numero ou sair: ")
        if number.lower() == 'sair':
            clear_terminal()
            print("Saindo do programa...")
            return

        if checker(number) is False:
            clear_terminal()
            print("Valor inválido, tente novamente.")
            continue

        while True:
            selector = input("Digite 1 para duplicar, 2 para triplicar, 3 para quadruplicar: ")
            clear_terminal()
            if selector == '1':
                print(f'O dobro de {number} é {duplicator(number)}')
                break
            elif selector == '2':
                print(f"O triplo de {number} é {triplicator(number)}")
                break
            elif selector == '3':
                print(f"O quadruplo de {number} é {quadruplicator(number)}")
                break
            else:
                print("Seleção inválida, tente novamente.")


        continuidade = input("Deseja continuar? (s/n): ")
        if continuidade.lower() != 's':
            clear_terminal()
            print("Saindo do programa...")
            return
        else:
            clear_terminal()

main()
