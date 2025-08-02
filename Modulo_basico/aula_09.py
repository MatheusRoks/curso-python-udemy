# esse é mais um exercicio, onde o usuário fornece seu peso, altura, idade e nome, e é feito um 
#calculo de imc.
#esse exercicio ainda poderia tratar mais erros, como idade fora de lógica, peso execessivo ou
#altura de um gigante, mas meu objetivo aqui é tentar entender o match case (que ainda não conhecia)
#e implementar sem o uso do if elif e else onde for possivel.

import os
def clear():
    os.system('cls' if os.name== 'nt' else 'clear')

user_data={
    'Nome':"",
    'Idade':0,
    'Altura':0.0,
    "Peso":0.0,
}
imc = 0.0
classificacao = ""

for key in user_data:
    match key:
        case "Nome":
            user_data["Nome"] = input(f'Digite seu {key}: ')
        case "Idade":
            while True:
                dado_inputado = input(f"Digite sua {key}: ")
                try:
                    user_data[key]=int(dado_inputado)
                    break
                except ValueError:
                    print("Digite numeros")
        case "Altura":
            while True:
                dado_inputado = input(f"Digite sua {key}: ")
                try:
                    user_data[key]=float(dado_inputado)
                    break
                except ValueError:
                    print("Digite numeros")
        case "Peso":
            while True:
                dado_inputado = input(f"Digite seu {key}: ")
                try:
                    user_data[key]=float(dado_inputado)
                    break
                except ValueError:
                    print("Digite numeros")

imc = user_data['Peso']/(user_data["Altura"]**2)
if  imc <= 18.5:
    classificacao = "Abaixo do peso"
elif imc > 18.5 and imc <= 24.9:
    classificacao = "Peso normal"
elif imc > 24.9 and imc <= 29.9:
    classificacao = "Sobrepeso"
elif imc > 29.9 and imc <= 34.9:
    classificacao = "Obesidade grau 1"
elif imc > 34.9 and imc <= 39.9:
    classificacao = "Obesidade grau 2"
else:
    classificacao = "Obesidade grau 3 (mórbida)"

clear()
print("\n--- Resultado do IMC ---")
print(f"Nome: {user_data['Nome']}")
print(f"Idade: {user_data['Idade']} anos")
print(f"Altura: {user_data['Altura']:.2f} m")
print(f"Peso: {user_data['Peso']:.2f} kg")
print(f"IMC: {imc:.2f}")
print(f"Classificacao: {classificacao}")