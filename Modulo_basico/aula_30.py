from clear import clear_terminal

def validar_cpf(cpf_str):

    cpf_numeros = ''.join(filter(str.isdigit, cpf_str))

    if len(cpf_numeros) != 11:
        return False
    
    if cpf_numeros == cpf_numeros[0]*11:
        return False
    
    cpf_soma = 0
    contador = 10

    for i in range(0,9):
        cpf_soma += ((int(cpf_numeros[i])) * contador )
        contador-=1

    first_digit = (cpf_soma*10)%11

    first_digit = first_digit if first_digit <=9 else 0

    if first_digit != int(cpf_numeros[9]):
        return False

    #segundo dígito
    contador = 11
    cpf_soma = 0

    for i in range(0,10):
        cpf_soma += ((int(cpf_numeros[i])) * contador )
        contador-=1

    second_digit = (cpf_soma*10)%11

    second_digit = second_digit if second_digit <=9 else 0
    
    if second_digit != int(cpf_numeros[10]):
        return False
    
    return True
def main():
    """
    Função principal que interage com o usuário para validar o CPF.
    """
    while True:
        clear_terminal()
        cpf = input("Digite seu CPF (apenas números, com ou sem pontuação): ").strip()
        
        if not cpf:
            print("Saindo do programa.")
            break

        if validar_cpf(cpf):
            print("\nO CPF é válido! 🎉")
        else:
            print("\nO CPF é inválido. Por favor, tente novamente.")
        
        input('\nPressione Enter para continuar...')

if __name__  == "__main__":
    main()