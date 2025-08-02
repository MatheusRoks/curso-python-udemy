#Tudo dentro do try será executado até que uma excessão(erro) ocorra
# ou seja se eu tiver o seguinte bloco
try:
    print('x1')
    print('x2')
    print(int('a'))
    print('x')
    print('x')
    print('x')
except:
    print('epa. erro')

#o x1 e x2 ainda serão executados. isso abre algumas oportunidades, como
#por meio de um erro induzido controlar o fluxo do programa, como em um and 
#não sei. ainda não sei bem onde eu usaria, ou se tem como usar, mas
#parece bem interessante