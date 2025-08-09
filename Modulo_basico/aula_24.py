#------------------------Desempacotando-------------------------

'''
O desempacotamento é uma forma de pegar o valor de uma lista e lançar ele numa variável
'''

#essa é a lista
name = ['matheus', 'antonio', 'maria', 'joão', 'jose']

#nesse momento, atribuí ao name1 o valor de matheus e ao *resto todo o restante da lista
name1, *resto = name

print(f'Veja, esse é o name1 {name1} e esse é o *resto, ', resto)

'''
por convenção, se é usado o _ para representar as variáveis que não serão usadas.

'''

#--------------------------------------TUPLA--------------------------------
'''
As tuplas são, basicamente, uma lista mas com a caracteristica de serem imutaveis.
o grande fator que nos faz utilizar a tupla, além dessa sua caracteristica de imutavel, é a sua
velocidade, que é maior que a da lista.

a tupla não recebe metodos

mas ainda assim é um iterável.

'''

exemplo_de_tuple = ('matheus', 'joão', 'jose', 1, 5, 10)
print(exemplo_de_tuple)


#---------------------enumarate-------------

'''
Para enumerar a lista e retornar ela + um numero, podemos usar o enumarate.  veja o exemplo

inclusive, podemos usar o start= para dizer apartir de qual numero começar a contagem.

ele sempre vai retornar uma tupla. porem ele tem uma particularidade. veja, após você utilizar
os dados que o seu iterator (no caso o enumarate) ele basicamente fica "vazio".
pense nele colo um deposito temporário, onde ele armazena os dados até serem usados 1x, dps disso
fica livre dnv. o jeito de contornar é exatamente fazer dessa forma: 

for i  in enumerate(name):
    print(i)

    
ainda, podemos usar o enumarate para pegar o index, usando do desempacotar. veja o exemplo
'''

lista_enumerada = enumerate(name)

for i  in lista_enumerada:
    print(i)

print(lista_enumerada)

for i  in enumerate(name):
    print(i)

for index, name in enumerate(name):
    print(index, name)