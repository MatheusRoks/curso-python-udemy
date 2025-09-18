import os


def check(lista):
    if len(lista) == 0:
        return True
    return False


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def erase_item(lista, lista_removidos):
    if check(lista):
        print(f'{BASICO} apagar.')
        return
    lista_removidos.append(lista[-1])
    lista.pop()
    return lista_removidos


def return_list(lista, lista_removidos):
    if check(lista):
        print(f'{BASICO} desfazer.')
        return
    lista.append(lista_removidos[-1])
    lista_removidos.pop()
    return lista


def show_list(lista):
    if check(lista):
        print(f'{BASICO} exibir.')
        return
    for i, item in enumerate(lista, start=1):
        print(f'{i}- {item}')


BASICO = "Você não possui itens na lista para"


continuar = True
num = 0
lista_ordenada = []
lista_removidos = []
while continuar:
    clear_screen()
    print(
        '''Os comandos disponíveis são:
        ver = mostra a lista;
        Apg = apagar o último item da lista;
        ret = dezfaz o apagar;
        Sair = sair do programa;
        ou apenas digite o que deseja adicionar à lista.''')
    item = input('O que deseja fazer? ').lower()
    match item:
        case 'ver':
            show_list(lista_ordenada)
            input('Aperte ENTER para continuar...')
        case 'apg':
            erase_item(lista_ordenada, lista_removidos)
            input('Aperte ENTER para continuar...')
        case 'ret':
            return_list(lista_ordenada, lista_removidos)
            input('Aperte ENTER para continuar...')
        case 'sair':
            show_list(lista_ordenada)
            input('Aperte ENTER para sair...')
            continuar = False
        case _:
            lista_ordenada.append(item)
