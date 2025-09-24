import os
import json


BASICO = "Você não possui itens na lista para"
continuar = True
lista_ordenada = []
lista_removidos = []

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_ARQUIVO = os.path.join(BASE_DIR, 'lista_ordenada.json')


def check(lista):
    return len(lista) == 0


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def erase_item(lista, lista_removidos):
    if check(lista):
        print(f'{BASICO} apagar.')
        return
    lista_removidos.append(lista.pop())
    return lista_removidos


def return_list(lista, lista_removidos):
    if check(lista_removidos):
        print(f'{BASICO} desfazer.')
        return
    lista.append(lista_removidos.pop())
    return lista


def show_list(lista):
    if check(lista):
        print(f'{BASICO} exibir.')
        return
    for i, item in enumerate(lista, start=1):
        print(f'{i}- {item}')


while continuar:
    if os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
            try:
                lista_ordenada = json.load(arquivo)
            except json.JSONDecodeError:
                lista_ordenada = []
    else:
        lista_ordenada = []

    clear_screen()
    print(
        '''Os comandos disponíveis são:
        ver  = mostra a lista;
        apg  = apagar o último item da lista;
        ret  = desfaz o apagar;
        sair = sair do programa;
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
            if not item.strip():
                print('Você não digitou nada. Tente novamente.')
                input('Aperte ENTER para continuar...')
                continue
            lista_ordenada.append(item)

    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(lista_ordenada, arquivo, indent=2, ensure_ascii=False)
