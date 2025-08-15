
def first_duplicate(lista):
    numeros_vistos = set()
    for number in lista:
        if number in numeros_vistos:
            return f'A duplicata é {number}'
        numeros_vistos.add(number)
    return "Sem duplicatas"

lista_de_numeros = [
    [1, 2, 3, 4,32, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4,3, 5, 6, 7, 8, 9, 10, 1],
    [1, 2, 3, 4, 5,5, 6,6, 7, 8, 9, 10, 11],
    [1, 2,1, 3, 4, 5, 6, 7, 8, 9, 10, 11,12, 12],
]

for i, lista in enumerate(lista_de_numeros):
    print(f'Lista {i+1}: {lista}')
    print(first_duplicate(lista))
