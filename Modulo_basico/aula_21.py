text = ' O python é uma linguagem de progrmação' \
        'multiparadigma' \
        'Python foi criado por Guido van Rossum'
count = 0
comparador = 0
letter = ''
text_without_spaces = text.replace(" ", "").lower()
for i in text_without_spaces:
    count = text_without_spaces.count(i)
    if count > comparador:
        comparador = count
        letter = i
print(f"A letra que mais se repetiu foi '{letter}' com {comparador} repetições")