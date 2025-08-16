#####vamos ver sobre lambda functions
#são funções anonimas e de uma unica linha

def order(item):
    return item['name']

name_list = [
    {'name': 'João', 'age': 20},
    {'name': 'Maria', 'age': 17},
    {'name': 'José', 'age': 18},
]

# name_list.sort(key=order)
# for item in name_list:
#     print(item)

#podemos fazer a mesma coisa com uma lambda function
# name_list.sort(key=lambda item: item['name'])
# for item in name_list:
#     print(item)

#esse exemplo é exatamente a memsa coisa que o anterior, mas com lambda, mas vamos traduzir o que está acontecendo. name_list é a nossa lista, o sort é o metodo que ordena a lista, key é o parametro que recebe uma função que irá ordenar a lista, e lambda é a função anônima que recebe o item da lista e retorna o valor do nome desse item. Assim, a lista é ordenada pelo nome de cada item. veja, para ficar ainda mais claro. name_list.sort(key=order) fala que a lista name_list deve ser ordenada usando a função order, que recebe um item e retorna o nome desse item. Já name_list.sort(key=lambda item: item['name']) faz a mesma coisa, mas usando uma função anônima (lambda) que recebe um item e retorna o nome desse item. Assim, ambas as linhas de código fazem a mesma coisa, mas de maneiras diferentes.
#ambos os exemplos acima atuam diretamente na lista original, mas podemos criar uma nova lista para que a ordenação seja feita e não altere o padrão.

# list_ordered = sorted(name_list, key=lambda item: item['name'])
# for item in list_ordered:
#     print(item)
# list_ordered2 = sorted(name_list, key=lambda item: item['age'])
# for item in list_ordered2:
#     print(item)

def execut(func, *args):
    return func(*args)

print(execut(lambda x, y: x+y, 2,3))
#print = execut = lambda 2 parametro, retorna o que esses parametros devem fazer, e apos isso recebe dois valores

double = (execut(lambda m: lambda n: n * m, 2))
print(double(2))

print(execut(lambda *args: sum(args), 1,2,3,6,4,8,2,10,2,0))