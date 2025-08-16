'''
vamos falar de list comprehension.

a list comprehension é uma forma de criar listas de forma curta.
nem sempre é a melhor forma de se criar listas, mas é uma otima forma de criar
listas de forma rápida e que possuam uma forma de filtragem ou lógica.

ela possui as seguintes estruturas:
[nome] = [
            [lógica]
            if [condição] else[outra condição]{modificação}
            for [variável] in [iterável]
            if [filtro]]
vamos ao exemplo de uma lista que multiplica numeros por 2 apenas se forem pares.

lista_pares = [
                number * 2 # lógica
                for number in range(10) #variável e iterável
                if number % 2 == 0 # filtro
 ]

 essa estrutuara é equivalente a:
lista_pares = []
for number in range(10):
    if number % 2 == 0:
        lista_pares.append(number * 2)

essas comprehensions são bemm uteis, assim como as funções lambda,
mas não são tão legíveis quanto o código tradicional.
use com moderação e sempre que possível, prefira o código tradicional.


'''

lista_pares = [
                number * 2
                for number in range(10) 
                if number % 2 == 0 
]

print(lista_pares)

#vamos a mais um exemplo, exibindo alterações em uma lista de dicionários
items = [
    {'name': 'item1', 'price': 10},
    {'name': 'item2', 'price': 20},
    {'name': 'item3', 'price': 30}
]
items_with_discount = [
    {**item, 'price': item['price'] * 0.9}  # aplicando desconto de 10%
    for item in items
]
print(*items_with_discount)
'''
o que está ocorrendo aqui, vou escrever de forma extensiva o que ocorre.
para cada item na lista de items, iremos desempacotar o item(que é um dicionário),
e a chave 'price' irá receber um desconto de 10% no valor de item['price'].


mas vamos complicar mais um pouco.
a estrutura de uma list comprehension é a seguinte:
[nome] = [
            [lógica]
            for [variável] in [iterável]
            if [filtro]
        ]

 mas podemos adcionar mais uma camada de condição, podemos adicionar um if else
 antes do for, veja o exemplo abaixo e dps a execução dele.
 [nome] = [
            [lógica]
            if [condição] else[condição padrão]{essa é a modificação}
            for [variável] in [iterável]
            if [filtro]
        ]

produtos = [
    {'name': 'produto1', 'price': 100},
    {'name': 'produto2', 'price': 200},
    {'name': 'produto3', 'price': 300}
]
produtos_com_desconto = [
    {**produto, 'price': produto['price'] * 0.9}
    if produto['price'] > 150 else produto
    for produto in produtos

'''

produtos = [
    {'name': 'produto1', 'price': 100},
    {'name': 'produto2', 'price': 200},
    {'name': 'produto3', 'price': 300}
]
produtos_com_desconto = [
    {**produto, 'price': produto['price'] * 0.9}
    if produto['price'] > 150 else produto
    for produto in produtos]
print(*produtos_com_desconto)

'''
os filtros são formas de eliminar itens indesejados da lista, ou seja, você
garante que apenas itens que atendem a condição estabelecida serão posteriormente 
adicionados e passarão pela condição e/ou passarão pela lógica

'''