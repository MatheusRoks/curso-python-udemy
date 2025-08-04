while True:
    name = input('digite seu nome: ')
    count = len(name)
    if name.isdigit() or count<=2:
        print("Por favor digite um nome válido")
        continue
    else:

        if count<=4:
            print(f'Seu nome possui {count} letras e é curto')
        elif count>=5 and count <=7:
            print(f'Seu nome possui {count} letras e é normal')
        else:
            print(f'Seu nome possui {count} letras e é grande')
    break
