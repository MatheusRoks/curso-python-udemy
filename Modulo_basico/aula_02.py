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