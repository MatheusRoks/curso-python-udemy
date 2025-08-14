from clear import clear_terminal

def checker(number):
    try:
        number = float(number)
        return True
    except ValueError:
        return False
    
def multipler(multiplier):
    def fmultiplier(number):
        return float(number) * multiplier
    return fmultiplier

duplicator = multipler(2)
triplicator = multipler(3)
quadruplicator = multipler(4)

while True:
    clear_terminal()
    print("Bem-vindo ao programa de duplicação, triplicação e quadruplicação de números!")
    number = input("Digite o numero que deseja multiplicar: ")
    if checker(number) is False:
        clear_terminal()
        print("Valor inválido, tente novamente.")
        continue
    option = input("Digite d para duplicar, t para triplicar ou q para quadruplicar: ").lower()
    match option:
        case 'd':
            print(f'O dobro de {number} é {duplicator(number)}')
        case 't':
            print(f"O triplo de {number} é {triplicator(number)}")
        case 'q':
            print(f"O quadruplo de {number} é {quadruplicator(number)}")
        case _:
            print("Opção inválida, tente novamente.")
    continuidade = input("Deseja continuar? (s/n): ")
    if continuidade.lower() != 's':
        clear_terminal()
        print("Saindo do programa...")
        break
    else:
        clear_terminal()