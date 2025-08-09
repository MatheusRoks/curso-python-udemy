# arredondadno númeross
'''
Ao realizar contas com números float, muitas vezes teremos alguma imprecisão na hora
de exibir o valor, mas podemos contornar isso, para isso vamos ter em conta 2 variaveis

'''
import decimal

number_1 = 0.7
number_2 = 0.1
number_3 = number_1 + number_2
print("Esse é o resultado sem formatação", number_3)
print("Agora vejamos o resultado formatado com uma f'")
print(f'Esse é o resultado formatado {number_3:.2f} ') #essa formatação sempre retorna
#uma str
print('Vejamos usando o a função round')#ela sempre retorna um inteiro
print(round(number_3, 2))
#a outra forma é com a biblioteca decimal. vejamos o exemplo
number_1 = decimal.Decimal("0.7")
number_2 = decimal.Decimal("0.1")
number_3 = number_1 + number_2
print("Esse é o resultado com a importação", number_3)