#dados boleanos -> boolean -> bool
#boolean é um outro tipo de dado em python que checa se a comparação/informação
# é True (verdadeira) ou False(falsa)

ok = True #repare que o sinal de atribuição foi usado e o dado que foi atribuido está em letra maiuscula, sem aspas e etc. por isso recebe o tipo boolena
print(type(ok))

"""
Junto do tipo boolean, possui os operadores lógicos que são usados com grande frequencia.
=    : significa atribuição, dá valor a uma variável ou constante
==    : comparação, verifica se os valores comparados são iguais
+    : soma de valores(numeros) ou concatenação(junção de str)
+=    : ex x=1|  x+=1 | x=2
-    :subtração
-=    :ex: x=3| x-=1 | x=2
*    : multiplicação
**    :exponenciação
!=    :verifica se os valores comparados sãoo DIFERENTES e retorna true se forem
/    :divisão que pode gerar numero float
//    :divisão que só gera numero int
%    :modulo, resto da divisão
>    :maior que
<    : menor que
>=    : maior ou igual a
<=    :menor ou igual a
*=    :mesmo esquema da +=, mas com multiplicação
/=    :mesmo do anterior mas com divisão
%=    :mesmo do anterior mas com módulo
vamos aos exemplos
"""
number_1 = 1 #aqui foi exemplificado a atribuição
number_2 = 1
number_3 = 2
number_4 = 20
number_5 = 3

print(number_1==number_2)#retorna true 
print(number_1!=number_2)#retorna false 
print(number_1+number_2)#retorna 2
print(number_1-number_2)#retorna 0
number_1+=2
print(number_1)#retorna 3 pos esssa variável foi alterada nesse momento
number_1-=2
print(number_1)#aqui volta a exibir 1 pois eu alterei mais uma vez a variável
print(number_1*number_5)#multiplicação
print(number_3**number_5)#exponenciação
print(number_4/number_3)#divisão que retorna float
print(number_4//number_3)#divisão que retorna int
print(number_4%number_3)#retorna o resto da divisão
print(number_3>number_4)#faz a comparadação de maior que
print(number_3>=number_4)#faz a comparadação de maior ou igual a
print(number_3<number_4)#faz a comparadação de menor que
print(number_3<=number_4)#faz a comparadação de menor ou igual
print("-"*10)
print("number_1 normal:",number_1)
number_1*=2
print("number_1 multipllicado por 2:",number_1)
print("-"*10)
print(number_1)
number_1/=2
print("number_1 dividido por 2:",number_1)
print("-"*10)
print(number_1)
number_1%=2
print("number_1 resto de uma divisão por 2:",number_1)
