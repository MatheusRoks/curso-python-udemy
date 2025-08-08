from clear import clear_terminal

password = "historiograficamente"
tentativas = 0
new_word = ""
letras_usadas = set()
letras_acertadas = ''
erros = 0
while new_word != password:
    new_letter = input('Digite uma letra: ')
    if len(new_letter) > 1:
        print('Por favor digite apenas uma letra')
        continue

    if erros >= 6:
        print(f"Você perdeu, a palavra era {password}")
        break
    
    if new_letter in letras_usadas:
        print('Você já digitou essa letra, tente outra')
        continue
    
    letras_usadas.add(new_letter)


    if new_letter in password:
        letras_acertadas += new_letter
    else:
        erros += 1

    new_word = ""    
    for i in password:
        if i in letras_acertadas:
            new_word += i
        else:
            new_word+="*"
    
    tentativas+=1


    clear_terminal()
    print(new_word)
    print(f'as letras usadas até o monento foram: {letras_usadas}')
else:
    print(f'Parabéns, você descobriu a palavra secreta que era {password}, em \
    {tentativas} tentativas')