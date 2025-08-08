from clear import clear_terminal

#variáveis
name = ''
new_name = ""
while True:
    name = input("Digite seu nome: ")
    clear_terminal()
    for letter in name:
        new_name = new_name + "*" + letter
    print(new_name + "*")
    break


