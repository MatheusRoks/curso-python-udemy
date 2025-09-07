"""
Range: utilizamos ele para gerar um contador FINITO, ou seja, ao criarmos ele
adicionamos automáticamente ao seu final a quantidade final.

count: é uma função do itertools, que não possui fim, por essa razão, ao criarmos
utilizamos o sistema de break e etc para ter certeza que não vai ficar infinitamente
rodando o código.

o mesmo princípio de star, step pode ser aplicado, infelizmente não o de final.
"""

from itertools import count

for i in count():
    if i >= 100:
        break
    print(i)
