verificacao = True
while verificacao:
    name = input('digite seu nome: ')
    if name.isdigit():
        print("Por favor digite apenas letras")
    else:
        count = len(name)
        if count<=4:
            print(f'Seu nome possui {count} letras e é curto')
            verificacao = False
        elif count>=5 and count <=7:
            print(f'Seu nome possui {count} letras e é normal')
            verificacao = False
        else:
            print(f'Seu nome possui {count} letras e é grande')
            verificacao = False
    
