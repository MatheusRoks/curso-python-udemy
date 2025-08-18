import sys

iteravel = [1,2,3,4,5,6,7,8,9]
iterator = iter(iteravel)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print("cabou")

#########################Generator

'''
Generator nada mais é que uma espécie de tuple comprehension, falo isso pela estrutura
mas sua grande vantagem é não salvar os valores na memoria do computador, o que torna mais leve. vamos ao exemplo pratico usando o modulo sys pra ver seu tamanho.

'''

lista = [n for n in range(10000000)]
gerador = (n for n in range(10000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(gerador))

