'''
Listas = tambem conhecidos como array, é uma froma de organizar dados,
as listas em python tão iteraveis e são modificaveis.
existem alguns tipos de metodos que as listas recebem.

a estrutura de uma lista é:

variavel = [1, 2, 3, 4, 5 ...]
porem uma peculiaridade das listas é a possibilidade de armazenar multiplos tipos
de valores, sejam eles str, int, float, bool e etc., ao mesmo tempo.

ex:

dados = ["matheus", 1.86, 23, True]

vamos aos metodos:

append: adiciona um novo elemento EM UMA LISTA JÁ EXISTENTE, esse metodo adiciona por
padrão o novo valor no final da lista.

insert: mesma funcionalidade do append, mas adiciona o item em um indice escolhido.

del: deleta um valor da lista inserindo o index do valor. Alem disso, você deve escrever esse códido fora de um print e etc

pop; por padrão remove o item do final da lista, mas pode remover o item do indice 
indicado. além disso, retorna o item, ou seja, além de remover, retorna o item 
removido

clear: literalmente limpa uma lista, remove todos os dados dela.

-------------------------atenção-------------------------------
todos esses metodos apresentados até o momento trabalham diretamente em uma lista
ou seja, você está literalmente alterando a lista principal.
isso em si não é um problema, se for realmente oq você quer, mas em alguns casos 
não é desejavel que isso ocorra, por isso temos a função copy.
--------------------------------------------------------------------

extend e concatenação
extend = basicamente junta duas listas em uma, POREM altera o valor das listas,
vamos ao exemplo. lista_c.extend(lista_d)
nesse caso, a lista c foi alterada, mas a lista d permanece normal.

ja a junção de listas com +(concatenação), pode evitar que os valores das listas sejam
alteradas tambem, você pode criar:

lista_z = lista_c + lista_d

assim, não haverá alteração em nenhuma lista, apenas a criação de uma nova lista

-----------------------------atenção------------------------------
no caso do extend e da concatenação, os valores passam a ser pertecentes a mesma
lista. mas se usar o append, você acaba de criar uma lista de listas, veja o exemplo


'''
lista_d = [4,4,4,4]
lista_c = [3, 3, 3, 3, 3]
lista_numeros = [1,2,3,4,5,6,7,8,9,10]
print(lista_numeros)
lista_numeros.append(32)
print("append, adicionando o 32", lista_numeros)
lista_numeros.insert(0,33)
print("insert, adicionando o 33", lista_numeros )
del lista_numeros[0]
print("del, removendo o indice 0", lista_numeros )
print("pop, removendo o indice 2,", lista_numeros.pop(2))

lista_b = lista_numeros.copy()
print("Essa é a copia",lista_b)
lista_c.extend(lista_d)
print("O extend", lista_c)
print("A lista_c.extend(lista_d) foi o resultado de cima veja agr a lista_d")
print(lista_d)
print("-" *30)
print("lista de listas")
lista_d.append(lista_c)
print(lista_d)