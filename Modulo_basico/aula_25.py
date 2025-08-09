from clear import clear_terminal

compras = []
comando = ''
parar = False
item = ''
comandos = ['adc', 'rm', 'parar', 'ver']
while parar is not True:
    comando = ''
    print('''
    lista de opções:
    - adc = adiciona um item a lista;
    - rm = remover um item;
    - parar = para o programa e mostra a lista;
    - ver = mostra a lista;
''')
    comando = input('digite uma opção: ').lower()
    if comando not in comandos:
        clear_terminal()
        print("Esse comando não é valido, favor digitar novamente")
        continue
    match comando:
        case 'parar':
            for index, name in enumerate(compras):
                print(index, name)
            break
        case "ver":
            for index, name in enumerate(compras):
                print(index, name)
        case "adc":
            item = input("Digite um item que deseja adicionar: ")
            compras.append(item)

