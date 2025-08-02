#vamos falar mais de f-str
#podemos usar alguns caracteres para realizar determinadas formatações em uma str
# > a esquerda
# < a direita 
# ^ ao centro
#
var = 'ABC'
print(f'{var: >10} a esquerda')#os sinais DEVEM ficar colados a quantidade
print(f'{var: <10} a direita')
print(f'{var: ^11} ao centro')
#podemos ainda usar e abusar do aspecto de formatação de numeros. veja
print(f'{10024000.5744554555:.2f}')#aquin ele limita as casas decimais exibidas
print(f'{10024000.5744554555:,.2f}')#aqui ele limita e ainda exibe , nas casas dos milhares
print(f'{10024000.5744554555:+,.2f}')#aqui limita, exibe e ainda exibe o sinal do numero
#mas não é necessário decorar isso afinal existem bibliotecas que fazem isso