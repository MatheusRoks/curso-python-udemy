'''
#######################import####################

vamos falar sobre a importação. para começo:
independentemente da forma que você importa, se é uma parte ou todo o modulo
o seu sistema terá o mesmo trabalho, então não immporta muito.

temos as seguintes formas:

1 forma: import alguma coisa = importa todo o módulo
a vantagem é que alem de ter todas as funções disponíveis, os nomes (namespaces) são
protegidos, o que quero dizer é, mesmo que você já possua uma variável com um mesmo
nome que uma função do modulo, você não corre o risco de sobrescrever nenhuma delas.
o problema é que os nomes ficam grandes.
ex:
import sys
print(sys.platform)

2 forma: from alguma coisa import isso, aquilo... = importa funções especificas daquele modulos. 
O beneficio é que os nomes ficam mais curtos, mas você pode acabar sobrescrevende a função ou sua variável.

ex:
from sys import platform

print(platform)

mas se eu tiver assim, sai antonio
from sys import platform

platform = 'antonio'

print(platform)

3 forma: from sys import*
isso importa TUDO no modulo mas impede de saber os nomes, deixa o código meio
obscuro pq não fica claro de onde cada coisa vem. enfim


'''

import sys
print(sys.platform)