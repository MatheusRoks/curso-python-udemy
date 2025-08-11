escola = [
    ['um', 'dois', 'tres', 'quatro'],
    ['cinco', 'seis', 'sete', 'oito'],
    ['nove', 'dez', 'onze', 'doze'],
    ['treze', 'quatorze', 'quinze', 'dezeseis'],
    ['dezessete', 'dezoito', 'dezenove', [20, 21, 22, 23]],
]

# for sala in escola:
#     print(f'A sala é: {sala}')
#     for numero in sala:
#         print(numero)


# para exibir todos os itens de uma lista sem as aspas é fácil
print(*escola[0])