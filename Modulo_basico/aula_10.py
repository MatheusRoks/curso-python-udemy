#aqui nessa aula meu objetivo é anotar sobre as f-strings e o .format.
#as f-strings possuem algumas coisas interessantes, uma delas é a possibilidade de
#na hora de exibir um dado, fromatar de froma mais rapida e limpa.
#supunhetamos que temos os seguintes dados.
# name = antonio
# age = 23
# height = 185cm
# caso desejemos usar o print, em python escreveremos da seguinte forma
# print(name + ' tem ' + age +' anos e sua altura é ' + height) forma normal em varias linguagens
# ou faremos assim print(name,'tem', age, 'anos e a sua altura é', height)
# agora caso usemos a f-string
# print(f'{name} tem {age} aos e sua altura é {heigt}')
# alem disso, em parametros com muitas casas decimais, podemos usar :.(numero de casas)f para
# limitar a exibição. vamos a um exemplo

count = 10/3
print(count)
print(f'{count:.2f}')

# e agora vamos ao format
# o format é um método, ele tambem vai auxiliar na formatação dos dados
# vamos aos exemplos e anotações
# vejamos algumas variáveis
a, b, c, d = 'um', 'dois', 'tres', 123.152 #sim, ao fazer isso, declaro varias variáveis em uma linha
#vamos ao formato
formatado = "x1={},x2={},x3={},x4={}".format(a,b,c,d)
#vamos ao print
print(formatado)
#x1=um,x2=dois,x3=tres,x4=123.152 esse foi o resultado. pq?
# primeiro definimos 4 variaveis, depois disso definimos uma variável chamada formato
# nessa variável formato, definimos uma str(esses x1 e etc) E ATRIBUIMOS ESSAS CHAVES as str
# apos isso usamos a função format e dizemos a ordem que os dados irão aparecer, vamos mudar a ordem
# para ficar mais claro
formatado = "x1={},x2={},x3={},x4={}".format(b,c,a,d)
#vamos ao print
print(formatado)
# x1=dois,x2=tres,x3=um,x4=123.152 esse foi o resultado. mas não acaba por ai
# podemos retirar esse x1 e etc e colocar ele dentro de uma str (uma tupla) e brincar um pouco mais
ordem = "x1={},x2={},x3={},x4={}"
formatado = ordem.format(b,c,a,d)
# vamos ao print
print(formatado)
#mas não acabou, dentro das chaves podemos passar ainda os indices (sendo o que se encontra dentro
#dos parentes do format a lista) e assim mudar a ordem de exibição direto na nossa tupla
ordem = "x1={0},x2={2},x3={3},x4={1}"
formatado = ordem.format(b,c,a,d)
# vamos ao print
print(formatado)
#ainda podemos usar o :.2f dentro dos parentes e ainda podemos exibir varias vezes o mesmo. veja
ordem = "x1={0},x1={0},x1={0},x1={0},x2={2},x3={3},x4={1}"
formatado = ordem.format(b,c,a,d)
# vamos ao print
print(formatado)
#x1=dois,x1=dois,x1=dois,x1=dois,x2=um,x3=123.152,x4=tres
#ainda assim temos que ter em mente que mesmo chamando por indice não é a melhor forma
#a melhor forma é por meio de paramentros e argumentos nomeados. vamos lla
ordem = "x1={name_1},x1={name_1},x1={name_1},x1={name_1},x2={name_4:.2f},x3={name_3},x4={name_2}"
formatado = ordem.format(
    name_1=a,
    name_2=b,
    name_3=c,
    name_4=d
)
print(formatado)

#só lembrando que str são iteraveis


# INTERPOLAÇÃO
#ainda nessee papo de formatação de str, temos algumas coisas interessantes para fazer.
# s = str
# d ou i = int
# f = float
# x ou X hexadecimal.
# vamos aos exeplos
name = 'antonio'
age = 19
variavel = "%s tem %i anos"%(name, age)
print(variavel)
#
#
#
#