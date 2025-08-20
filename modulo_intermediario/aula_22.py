##########módulos##########
'''
além dos modulos padrão do py, podemos, e vamos, usar os nossos proprios modulos.
por padrão, o arquivo main(o arquivo onde a execução começou) não consegue identificar
modulos acima dele. Ex:
nesse mesmo curso temos dois pacotes até o momento, o pacote modulo_basico e o
modulo_intermediário.

é possivel ver com clareza que esses arquivos não se comunicam diretamente só pela 
nomeação, veja, em ambos temos aula_01 por exemplo, o que não é possível dentro
de um mesmo pacote. Assim sendo, por padrão, não posso importar modulos que não este-
jam no mesmo pacote ou que sejam padrão. Claro, isso por padrão.

por essa razão, ao se pensar em criar um sistema, vamos criar ele sempre entorno do 
modulo main, o seu modulo principal. Isso garante uma organização e uma facilitade.

porem, atenção, pacotes dentro de outros pacotes podem ser acessados. como assim?
veja, dentro do pacote modulo_intermediario criei um pacote chamado teste_01. veja o que posso fazer aqui.

from teste_01 import say_hi

ele basicamente exeutou o modulo. Então pacotes internos é possivel de ser executado.
mas pacotes externos não. Confuso? talvez, mas pense assim. você tem uma grande sacola
dentro dessa sacola você possui 3 sacolas menores, finjamos que essas sacolas menores
tem doces dentro. Por lógica, os doces estao dentro da sacola menor mas estão
tambem dentro da sacola maior, certo? então da pra dizer que os doces pertecem a sacola
maior.
mas a sacola maior pertence as sacolas menores? não. 
é a mesma coisa, de dentro do modulo teste_01 não consigo, por padrão, usar o meu clear.
'''
    
from teste_01 import say_hi



