from clear import clear_terminal
import random
import time

def gerador_cpf(quantidade):
    start = time.time()
    vezes=0
    while quantidade > vezes:
        vezes+=1

        nove_digitos = ""
        for i in range(9):
            nove_digitos += str(random.randint(0,9))

        cpf_soma = 0
        contador = 10

        for i in range(0,9):
            cpf_soma += ((int(nove_digitos[i])) * contador )
            contador-=1

        first_digit = (cpf_soma*10)%11

        first_digit = first_digit if first_digit <=9 else 0

        dez_digitos = nove_digitos + str(first_digit)

        #segundo dígito
        contador = 11
        cpf_soma = 0

        for i in range(0,10):
            cpf_soma += ((int(dez_digitos[i])) * contador )
            contador-=1

        second_digit = (cpf_soma*10)%11

        second_digit = second_digit if second_digit <=9 else 0
        cpf_gerado = dez_digitos + str(second_digit)

        cpf_formatado = f"{cpf_gerado[:3]}.{cpf_gerado[3:6]}.{cpf_gerado[6:9]}-{cpf_gerado[9:]}"
        print(cpf_formatado)
        print("-"*20)
    end = time.time()
    print(f'O programa levou {end - start} para ser executado')
def main():
    """
    Função principal que interage com o usuário para validar o CPF.
    """
    while True:
        clear_terminal()
        quantidade = input("Digite quantos cpf's deseja gerar: ")
        
        if not quantidade:
            print("Saindo do programa.")
            break

        if quantidade.isdigit():
            quantidade = int(quantidade)
            gerador_cpf(quantidade)
        else:
            continue

        input('\nPressione Enter para continuar...')

if __name__  == "__main__":
    main()

