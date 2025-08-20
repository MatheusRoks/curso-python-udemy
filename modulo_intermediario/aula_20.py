name = 'matheus'
number1 = 10
number2 = 0
number3 = 2
try: 
    print(name[20])
except ZeroDivisionError:
    print('Erro, divisão por 0')
except NameError:
    print("Erro, variável não definida")
except(TypeError, IndexError) as error:
    if error.__class__.__name__ == "IndexError":
        print('Erro de indice')
    else:
        print('erro de tipagem')


'''
except trata erros, esses devem ser tratados sempre, não se deve usar 
try:
    ...
except:
    ...
o except deve receber o nome do erro.

temos o finally, ele SEMPRE será executado, mesmo que haja um erro

'''

try:
    number1/number2
except ZeroDivisionError:
    print('erro, divisão por 0')
finally:
    print("cabou")  

'''
ainda da pra colocar um else ai se tudo ocorrer direito, antes do finally, o else
será executado.

é possivel levantar uma excessão usando o raise
'''