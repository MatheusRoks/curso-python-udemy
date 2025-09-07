from itertools import zip_longest

local = ["salvador", "ubatuba", "belo horizonte"]
estado = ['Ba', "Sp", "Mg", "rj"]


def zipper(lista, lista2):
    escolha = min(len(lista), len(lista2))
    return [(lista[i], lista2[i]) for i in range(escolha)]


print(zipper(local, estado))
print(list(zip(local, estado)))
print(list(zip_longest(local, estado)))
