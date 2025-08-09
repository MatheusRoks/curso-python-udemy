#split e join
'''
são metodos de uma str, basicamente facilitam a nossa vida.

o split "quebra" a str em algumas partes e retorna uma lista de palavras.
se eu não passar nada denttro do split, ele irá quebrar a cada espaço em brancp
caso eu deseje, posso passar uma virgula, ou ponto, ou qualquer outro sinal e 
a cada vez que ele encontrar esse sinal, ele quebrará a frase.
'''
frase = 'Olha só que legal, posso partir ela em vários pedaços'
lista_palavras = frase.split()
print("A nova lista", lista_palavras)