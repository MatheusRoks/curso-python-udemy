#a função print imprime um valor na tela do usuário. 
# por caracteristica padrão do python, cada print novo gera automáricamente
#uma quebra de linha. Além de adicionar um separador dentro do conteúdo ao usar ,
print(12, 34)
print(56, 78)
print(90, 11)
# esse código vai exibir
#12 34
#56 78
#90 11

#Posso ainda modificar o separador da função print.
print(1, 2, 3, 4, sep="")   #1234
print(1, 2, 3, 4, sep=" ")  #1 2 3 4
print(1, 2, 3, 4, sep="-")  #1-2-3-4
print(1, 2, 3, 4, sep=",")  #1,2,3,4
print(1, 2, 3, 4, sep=".")  #1.2.3.4

#além disso, posso manualmente solicitar quebras de linha por meio do
#\r\n

print("hello \r\nworld")
'''
esse código irá imprimir
hello
world

pois usei  o \r\n para adicionar uma quebra no meio da frase.
ainda posso usar o \n, pois meu windows não é tão antigo e já interpreta.

CRLF -> \r\n;
LF -> \n
'''

#além desses detalhes, posso modificar o final dos print exibibindo outro elemento.

print(1, 2, 3, 4, sep="", end="\r\n")   #1234
print(1, 2, 3, 4, sep=" ", end="-")  #1 2 3 4-1-2-3-4#1,2,3,4
print(1, 2, 3, 4, sep="-", end="#")  
print(1, 2, 3, 4, sep=",", end='\n')  
print(1, 2, 3, 4, sep=".", end="oi")  #1.2.3.4oi

'''
além disso, posso adicionar o \r\n junto do elemento end, para gerar ainda mais
modificações
'''
print("\noi", end=", \n")
print("tudo bem?")
'''
sendo a exibição
oi,
tudo bem?
'''