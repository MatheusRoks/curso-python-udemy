while True:
    time = input("Digite o horário atual(apenas a hora): ")
    try:
        time = int(time)
        if time < 0 or time > 23:
             print('horário inválido, digite novamente')
        else:
            break
    except ValueError:
        print('Digite apenas números')

if time  < 12:
        print("Bom dia")
elif time >= 12 and time <= 18:
     print('Boa tarde')
else:
     print('Boa noite')