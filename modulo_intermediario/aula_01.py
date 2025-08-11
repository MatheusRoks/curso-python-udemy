#-------------------------------funções
''' 
as funções são formas de evitar repetição no código,
além de alterar o fluxo do código.

as funções podem receber parametros e esses parametros quando recebem um valor
são chamados de argumentos.

pense assim:
teste = 123
essa é a forma que definimos nossa variável, o nome da variável
é o parametro e o valor é o argumento

'''
def imprimir(a,b,c):
    print("foi executado", a, b, c)

imprimir(1,2,3)

"""
é possivel atribuir um valor padrão para um parametro, veja o exemplo
"""

def numeros(a=1,b=10,c=100):
    print(a,b,c)

numeros()
numeros(30,60,90)

#-------------------Argumentos nomeados ------------
'''
caso voce use os argumentos da forma que foi mostrada acima, isso é chamado de 
argumentos posicionais, a ordem que esses argumentos são enviadas importa.
ou seja, o primeiro valor será indicado para a, o segundo para b e etc.

mas caso você não deseje que isso ocorra, você pode enviá-los da seguinte forma
def numeros(a=1,b=10,c=100):
    print(a,b,c)

numeros(b=30,c=60,a=90)

com isso, você está basicamente mudando a forma que ele será exibido. irei mostrar
'''
numeros(b=30,c=60,a=90)