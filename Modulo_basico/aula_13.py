import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

user_data={
    'nome': '',
    'idade': 0,
}
other={
    'invertido':'',
    'espaço':'',
    'letras':'',
    'primeira letra': '',
    'ultima letra':'',
}

for key in user_data:
    match key:
        case 'nome':
            while True:
                name = input('Digite seu nome: ')
                if not name.isdigit():
                    user_data[key] = name
                    break
                else:
                    print('Entrada invalida, favor digitar seu nome')
        case 'idade':
            while True:
                try: 
                    age = input("Digite sua idade: ")
                    age = int(age)
                    if age > 0 and age <=120:
                        user_data[key]=age
                        break
                    else:
                        print('Digite uma idade válida')
                except ValueError:
                    print('Apenas números são aceitos')

for key in other:
    match key:
        case 'invertido':
            other[key]=user_data['nome'][::-1]
        case 'espaço':
            other[key] = ('sim' if ' ' in user_data['nome'] else 'não')
        case 'letras':
            other[key] = len(user_data['nome'])
        case 'primeira letra':
            other[key] = user_data['nome'][0]
        case 'ultima letra':
            other[key] = user_data['nome'][-1]

new_user_data = user_data | other

clear_terminal()

print("_"*20)
for key, value in new_user_data.items():
    print(f'{key}: {value}')
    print("_"*20)
