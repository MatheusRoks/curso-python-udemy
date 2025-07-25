#como esses arquivos são referentes ao meus estudos e conhecimentos, irei usar nesse exercício alguns elementos mais avançado, pois busco treinar.
#todos os meus exercicios serão desse nível a mais, afinal, desejo treinar meus conhecimentos.

import os #importei a biblioteca só para usar o sistema de limpeza do terminal
import datetime #biblioteca usada para saber o ano em que estamos

'''uma função para evitar quebra em outros sistemas operacionais'''
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#isso abaixo nada mais é que um dicionário com chaves, mas vazio de valor
user_form={
    "nome":"",
    "sobrenome":"",
    "idade":"", #será ignorado durante o loop
    "ano de nascimento":"",
    "Maioridade?":"", #será ignorado durante o loop
    "altura":"",
}


#serve para percorrer todo o dicionário e adicionar os novos valores ao dicionário,, além de lógica de confirmação
for key in user_form:
    if key == "ano de nascimento":
        while True:
            try:
                ano_de_nascimento = input(f'Informe seu {key}: ')
                ano_de_nascimento= int(ano_de_nascimento)
                if ano_de_nascimento <=1900 or ano_de_nascimento > datetime.datetime.now().year:
                    print("digite um dado válido")
                else:
                    user_form[key]=ano_de_nascimento
                    user_form['idade']= datetime.datetime.now().year -ano_de_nascimento
                    break
            except ValueError:
                print("Por favor, digite um número válido")
    elif key == "altura":
        while True:
            altura = input(f'Informe sua Altura(em cm): ')
            if altura.isdigit():
                altura = int(altura)
                user_form[key] = altura
                break
            else:
                print("Digite apenas valores numéricos e sem ponto")
    elif key == "Maioridade?" or key=="idade":
        continue
    else:
        user_form[key] = input(f'Informe seu {key}: ')

if "idade" in user_form and isinstance(user_form['idade'], int):
    user_form["Maioridade?"] = "sim" if user_form['idade'] >= 18 else "não"
else:
    print("não é possivel determinar a maioridade")
    user_form["Maioridade?"] = "não consegui determinar."

#forma de limpar o terminal para que os antigos input não sejam exibidos
clear_terminal()

#forma de apresentar o dicionário de forma mais eficiente
for key, value in user_form.items():
    print(f'{key}: {value}')