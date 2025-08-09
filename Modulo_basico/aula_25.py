from clear import clear_terminal

def ver():
    for index, name in enumerate(compras, start=1):
        print(index, name)

def parar():
    clear_terminal()
    ver()
    return False

def verification(remove):
    try:
        remove = int(remove)
        remove -= 1
        compras.pop(remove)
    except ValueError:
        print("Digite apenas números ao remover itens")
    except IndexError:
        print("Esse item não existe")


compras = []
comando = ''
pare = True
remove = 0
comands = '''
    --- MENU DE OPÇÕES ---
    - rm: Remover um item
    - ver: Exibir a lista
    - parar: Sair do programa
    ----------------------'''

while pare:
    print(comands)
    comando = input("Digite um item que deseja adicionar ou um comando: ")
    if comando == 'parar':
        pare = parar()
    elif comando == 'ver':
        clear_terminal()
        ver()
    elif comando == 'rm':
        while remove != 'stop':
            ver()
            print("Caso deseje parar digite: stop")
            remove = input('Digite o número do item que deseja remover: ').lower()
            if remove == 'stop':
                continue
            clear_terminal()
            verification(remove)

    else:
        compras.append(comando)
        clear_terminal()

