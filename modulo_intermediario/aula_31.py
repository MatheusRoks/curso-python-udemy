from functools import reduce


def fu_reduce(acumulator, product):
    return (acumulator + product['preço'])


products = [
    {'nome': "produto 1 ", 'preço': 10.00},
    {'nome': "produto 2 ", 'preço': 32.55},
    {'nome': "produto 3 ", 'preço': 15.98},
    {'nome': "produto 4 ", 'preço': 80.57},
    {'nome': "produto 5 ", 'preço': 1.98},
    {'nome': "produto 6 ", 'preço': 98.85},
    {'nome': "produto 7 ", 'preço': 1455.98},
    {'nome': "produto 8 ", 'preço': 98.99},
]

total = reduce(
    fu_reduce,
    products,
    0
)

print(total)
