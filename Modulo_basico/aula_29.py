'''
-----------------------------------operação ternária-------------------
a operação ternária é uma das formas de facilitar a escrita do código.

<valor> if <condição> else <outro valor>

aqui está dizendo basicamente isso:

if condição:
    <valor>
else:
    <outro valor>

'''

valor = 'Olá, bem-vindo'
outro_valor = 'Tchau'
condicao = None
condicao = input("Digite chegou para sinalizar que chegou ou qualquer outra coisa \
para a saída: ")
True if condicao == "Chegou" else False
print(valor if condicao else outro_valor)