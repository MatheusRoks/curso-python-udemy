import copy
from print import p_print


def incrase_by_10(number):
    return round(number * 1.10, 2)


def apply_increase_by_10(product):
    for i in product:
        number = i['preço']
        i['preço'] = incrase_by_10(number)
    return product


def sort_products(products, key_name, order=False):
    ordenated = sorted(
        products, key=lambda name: name[key_name], reverse=order)
    return ordenated


product = [
    {'nome': "produto 1 ", 'preço': 10.00},
    {'nome': "produto 2 ", 'preço': 32.55},
    {'nome': "produto 3 ", 'preço': 15.98},
    {'nome': "produto 4 ", 'preço': 80.57},
    {'nome': "produto 5 ", 'preço': 1.98},
    {'nome': "produto 6 ", 'preço': 98.85},
    {'nome': "produto 7 ", 'preço': 1455.98},
    {'nome': "produto 8 ", 'preço': 98.99},
]

new_price = copy.deepcopy(product)
new_price = apply_increase_by_10(new_price)
by_name = copy.deepcopy(new_price)
by_price = copy.deepcopy(new_price)
by_name = sort_products(by_name, "nome", True)
by_price = sort_products(by_price, 'preço')

p_print('Lista original dos produtos', product)
print('\n')
p_print("lista com os preços alterados", new_price)
print('\n')
p_print("lista com os nomes ordenados", by_name)
print('\n')
p_print("lista com o preço ordenado", by_price)
