'''
conversão de tipos ou:
coerção;
coercion;
type convertion;
typecasting.

basicamente é cnverter um dado em outro QUANDO POSSIVEL vamos aos exemplos.
'''

name = "matheus" #str
age = 19 #int
weight = 110.00 # float
majority = "sim" #str
#veja os type
print(name, type(name))
print(age, type(age))
print(weight, type(weight))
print(majority, type(majority))
print("-"*20)
#vamos alterar age para float e dps para str, weight para int e majority para bool
print(name, type(name))
print(float(age), type(float(age)))#só preciso colocar a coerção dentro do type
print(str(age), type(str(age))) # porque não alterei a variável em si, se eu
print(int(weight), type(int(weight))) #printar a variável e ainda solicitar o type
print(bool(majority), type(bool(majority)))# ele vai apresentar o mesmo valor que 
print("-"*20) #discriminado antes dos -------------
