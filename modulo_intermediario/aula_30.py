from functools import partial
from print import p_print


def plus(price, porcent):
    return round(price * porcent, 2)


plus_ten = partial(
    plus,
    porcent=1.1
)


def priniter(iterator):
    print(*list(iterator), sep='\n')
    print()


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

filtrado = filter(
    lambda p: p['preço'] > 10,
    products
)


def change(product):
    return {**product, "preço": plus_ten(product['preço'])}


new_product = map(change, products)

priniter(new_product)
