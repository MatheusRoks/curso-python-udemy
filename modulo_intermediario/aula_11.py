#set, os diagramas de ven do python
# os set são conjuntos de dados que se assemelha a uma lista
# ele é um iterável, mas não é indexado
# além disso, não aceita valores duplicados
# então, caso deseje facilmente remover valores duplicados de uma lista
# fazer o typecoertion para set é uma boa opção
# porem uma particularidade do set é que ele não mantém a ordem dos elementos   
# e não aceita valores mutáveis como listas ou dicionários
# as formas de criar um set são:
# set() ou {1, 2, 3, 4, 5}
# para adicionar valores a um set, usamos o método add()
# para remover valores, usamos o método remove() ou discard()
# o método remove() gera um erro se o valor não existir, enquanto discard() não gera erro
#mas como ele não é indexado, para remover um valor específico, precisamos saber o valor exato
# podemos verificar se um valor está presente no set usando o operador in
# para iterar sobre os valores de um set, usamos um loop for
# podemos também usar a função len() para obter o tamanho do set
# e a função clear() para remover todos os elementos do set
#vamos aos exemplos

set1 = set('matheus')
set2 = { 1, 2, 3, 4, 5, 6, 7, 8, 9}


#vamos aos médotodos entre os sets
#união
set3 = set1 | set2
set3 = set1.union(set2)
print(set3)
#interseção
set3 = set1 & set2
set3 = set1.intersection(set2)
print(set3)
#diferença
set3 = set1 - set2
set3 = set1.difference(set2)
print(set3)
#diferença simétrica
set3 = set1 ^ set2
set3 = set1.symmetric_difference(set2)
print(set3)
#verificação de subconjunto
set3 = set1 <= set2
set3 = set1.issubset(set2)
print(set3)
#verificação de superconjunto
set3 = set1 >= set2
set3 = set1.issuperset(set2)
print(set3)
#verificação de disjunção
set3 = set1.isdisjoint(set2)
print(set3)
#verificação de igualdade
set3 = set1 == set2
print(set3)
#verificação de desigualdade
set3 = set1 != set2
print(set3)
#cópia
set3 = set1.copy()
print(set3)
#remoção de elementos
set1.remove('m')
print(set1)
set1.discard('a')
print(set1)
set1.discard('z') #não gera erro
print(set1)
#limpeza do set
set1.clear()
print(set1)
#tamanho do set
set3 = len(set2) 
print(set3) 
#verificação de presença
set3 = 'matheus' in set2
print(set3) 