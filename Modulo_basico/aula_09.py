# esse é mais um exercicio, onde o usuário fornece seu peso, altura, idade e nome, e é feito um 
#calculo de imc.

user={
    'Nome':"",
    'Idade':"",
    'Altura':"",
    "Peso":"",
}
for key in user:
    match user[key]:
        case "Nome":
            user["Nome"] = input(f'Digite seu {user[0]}: ')
        case "Idade":
            user[1] = input(f'Digite sua {user[1]}: ')