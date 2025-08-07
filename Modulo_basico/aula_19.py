from clear import clear_terminal

#variáveis
name = ''
while True:
    name = input("Digite seu nome: ")
    clear_terminal
    for letter in name:
        print("*",letter,end='', sep="")
    print("*")
    break


