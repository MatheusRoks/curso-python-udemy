'''
##################### dicionário #####################
vamos falar sobre os dicionários em python.
# dicionários são estruturas de dados que armazenam pares de chave-valor
# eles são mutáveis, ou seja, podemos alterar seus valores após a criação
# eles são definidos com chaves {} e os pares de chave-valor são separados por vírgulas
# exemplo de dicionário

pessoa = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'São Paulo'
}

vamos ao exemplo:
'''

pessoa = {
    'nome': 'João',
    'idade': 30,
    'altura': 1.75,
    'habilidades': ['programação', 'matemática', 'física'],
    'endereco': [{'rua': 'Rua A', 'numero': 123}, {'rua': 'Rua B', 'numero': 456}],
    'ativo': True,
    'contatos': {
        'email': '',
        'telefone': '1234-5678',
        'endereco': {
            'rua': 'Rua C',
            'numero': 789,
            'cidade': 'São Paulo',
            },
        },
} 

print(pessoa)#nisso pego o dicionário inteiro
print(pessoa['nome'])#nisso pego o nome
print(pessoa['endereco'])#nisso pego endereço
print(pessoa['habilidades'][1])

'''
alem desses aspctos, temos outros métodos interessantes:
# adicionar um novo par chave-valor
pessoa['peso'] = 70 
# alterar um valor existente
pessoa['idade'] = 31 
# remover um par chave-valor
del pessoa['cidade'] 
# verificar se uma chave existe
if 'nome' in pessoa:
    print('Nome existe no dicionário')
# obter todas as chaves
chaves = pessoa.keys()
# obter todos os valores
valores = pessoa.values()
# obter todos os pares chave-valor
itens = pessoa.items()
# limpar o dicionário
pessoa.clear()
# remover e retornar um valor
idade = pessoa.pop('idade', None)
# remover e retornar o último par chave-valor adicionado
ultimo_item = pessoa.popitem() 


'''

#iterando sobre dicionários
print('\nIterando sobre dicionários:')
print("-"*30)
for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')

print("-"*30)
#outra forma de iterar
for chave in pessoa:
    print(f'{chave}: {pessoa[chave]}')
print("-"*30)
#outra forma de iterar
for valor in pessoa.values():
    print(valor)
print("-"*30)
#outra forma de iterar
for chave in pessoa.keys():
    print(chave)
print("-"*30)
#outra forma de iterar
for chave in pessoa:
    print(chave)
    print(pessoa[chave])
print("-"*30)
#outra forma de iterar
for i in range(len(pessoa)):
    chave = list(pessoa.keys())[i]
    valor = pessoa[chave]
    print(f'{chave}: {valor}')
print("-"*30)
#outra forma de iterar
for i, (chave, valor) in enumerate(pessoa.items()):
    print(f'{i}: {chave} = {valor}')

print("-"*30)
"""
quando desejamos usar o if no dicionário, podemos fazer assim:
if pessoa.get('nome')is not None:
    print('Nome existe no dicionário')
else:
    print('Nome não existe no dicionário')

vamos falar dos metódos:
len() - retorna o número de itens no dicionário
keys() - retorna uma visão das chaves no dicionário
values() - retorna uma visão dos valores no dicionário
items() - retorna uma visão dos pares chave-valor no dicionário
get() - retorna o valor para uma chave específica, ou None se a chave não existir
update() - atualiza o dicionário com pares chave-valor de outro dicionário ou de um iterável de pares chave-valor
clear() - remove todos os itens do dicionário
pop() - remove o item com a chave especificada e retorna seu valor, ou um valor padrão se a chave não existir
popitem() - remove e retorna um par chave-valor arbitrário do dicionário
setdefault() - retorna o valor para uma chave específica, e se a chave não existir, insere a chave com um valor padrão

"""