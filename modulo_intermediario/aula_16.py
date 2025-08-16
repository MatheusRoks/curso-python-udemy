from print import p_print

lista = [
    (number1, number2)
    for number1 in range(3)
    for number2 in range(3)
]
p_print(lista)