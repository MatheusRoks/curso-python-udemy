#split, strip e join
'''
são metodos de uma str, basicamente facilitam a nossa vida.

o split "quebra" a str em algumas partes e retorna uma lista de palavras.
se eu não passar nada denttro do split, ele irá quebrar a cada espaço em brancp
caso eu deseje, posso passar uma virgula, ou ponto, ou qualquer outro sinal e 
a cada vez que ele encontrar esse sinal, ele quebrará a frase.

strip: remove espaços excedentes. se eu passar apenas strip() remove no comeco e no fim,
caso eu passe rstrip() apenas no fim
lstrip() apenas no inicio

o join muda a forma que os itens de um iteravel são separados e retorna tudo em uma
str
'''


frase_crua = 'Olha só que legal, posso partir ela em vários pedaços'
lista_palavras = frase_crua.split()
lista_organizada = []
print("A nova lista", lista_palavras)
#vamos a mais exemplos
lista_palavras = frase_crua.split(',')
for i, frase in enumerate(lista_palavras):
    print(lista_palavras[i].strip())

for i, frase in enumerate(lista_palavras):
    lista_organizada.append(lista_palavras[i].strip())

str_join = "-".join(lista_organizada)
print(str_join)