from clear import clear_terminal

def ver():
    clear_terminal()
    for index, name in enumerate(compras, start=1):
        print(index, name)

def parar():
    ver()
    return False

def verification(remove):
    try:
        remove = int(remove)
        remove -= 1
        compras.pop(remove)
    except ValueError:
        print("Digite apenas números ao remover itens")


compras = []
comando = ''
pare = True
item = ''
remove = 0
comands = '''
    --- MENU DE OPÇÕES ---
    - rm: Remover um item
    - ver: Exibir a lista
    - parar: Sair do programa
    ----------------------'''

while pare:
    print(comands)
    item = input("Digite um item que deseja adicionar: ")
    if item == 'parar':
        pare = parar()
    elif item == 'ver':
        ver()
    elif item == 'rm':
        while remove != 'stop':
            ver()
            print("Caso deseje parar digite: stop")
            remove = input('Digite o número do item que deseja remover: ').lower()
            if remove == 'stop':
                continue
            verification(remove)

    else:
        compras.append(item)
        clear_terminal()

