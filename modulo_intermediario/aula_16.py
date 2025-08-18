from print import p_print

lista = [
    (number1, number2)
    for number1 in range(3)
    for number2 in range(3)
]
print(lista)

product = {
    'name': 'caneta',
    'price': 2.50,
    'local': 'escritório'
}
#o filtro de dict comprehension é o inverso dos outros, apenas adiciona aquilo que ele
#filtra se você colocar o ==, e != para tudo que não é aquela chave vou usar price como filtro
dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in product.items()
    if chave != 'price'
}

p_print(dc)