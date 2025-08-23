# mais uma vez peguei meu código, enviei na ia e copiei, pra aprender com ela
# como implementar algumas coisas

import copy
from print import p_print
import matplotlib.pyplot as plt


def increase_by_10(number):
    """Aumenta o valor em 10% e arredonda para 2 casas decimais"""
    return round(number * 1.10, 2)


def apply_increase_by_10(products):
    """Aplica o aumento de 10% em todos os preços"""
    for item in products:
        item['preço'] = increase_by_10(item['preço'])
    return products


def sort_products(products, key_name, order=False):
    """Ordena os produtos pela chave informada (nome ou preço)"""
    return sorted(products, key=lambda x: x[key_name], reverse=order)


def show_graph(products):
    """Exibe gráfico de barras com os preços dos produtos"""
    nomes = [p['nome'] for p in products]
    precos = [p['preço'] for p in products]

    plt.figure(figsize=(10, 5))
    plt.bar(nomes, precos, color="skyblue", edgecolor="black")

    plt.title("Preço dos Produtos (com aumento de 10%)")
    plt.xlabel("Produto")
    plt.ylabel("Preço (R$)")
    plt.xticks(rotation=45)

    # Adiciona valores em cima das barras
    for i, v in enumerate(precos):
        plt.text(i, v + (max(precos) * 0.01), f"R${v:.2f}", ha="center")

    plt.show()


# Lista inicial de produtos
product = [
    {'nome': "produto 1", 'preço': 10.00},
    {'nome': "produto 2", 'preço': 32.55},
    {'nome': "produto 3", 'preço': 15.98},
    {'nome': "produto 4", 'preço': 80.57},
    {'nome': "produto 5", 'preço': 1.98},
    {'nome': "produto 6", 'preço': 98.85},
    {'nome': "produto 7", 'preço': 1455.98},
    {'nome': "produto 8", 'preço': 98.99},
]

# Copiar e aplicar aumento
new_price = copy.deepcopy(product)
new_price = apply_increase_by_10(new_price)

# Ordenações
by_name = sort_products(copy.deepcopy(new_price), "nome", True)
by_price = sort_products(copy.deepcopy(new_price), "preço")

# Impressão
p_print('Lista original dos produtos', product)
print("\n")
p_print("Lista com os preços alterados", new_price)
print("\n")
p_print("Lista com os nomes ordenados", by_name)
print("\n")
p_print("Lista com o preço ordenado", by_price)

# Extra: mostrar gráfico
show_graph(new_price)
