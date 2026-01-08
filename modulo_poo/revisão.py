# criando classes

# As classes geram novos objetos, possuindo seus atritubos e métodos proprios

'''
para criar uma classe, utilizamos a palavra reservada class seguida do nome da classe e dois pontos.
por convenção, o nome das classes começam com letra maiúscula e utiliza o estilo
PascalCase.

toda a classe possui um método de iniciação da classe, normalmente é utilizado o método __init__. o primeiro parãmetro desse método sempre será o self (palavra usada por convenção, mas seja o nome que for, ele sempre será a instância da própria classe). Os outros parâmetros são os atributos que a classe terá.

'''


# class Pessoa:
#     def __init__(self, nome, sobrenome, idade):
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.idade = idade

#     def Saudacao(self):
#         print(
#             f'Olá, meu nome é {self.nome} {self.sobrenome} e tenho {self.idade} anos.')

#     def acao(self, iacao):
#         print(f'{self.nome} está {iacao}.')


# p1 = Pessoa('Matheus', 'Roks', 23)
# # print(p1.nome)
# # print(p1.sobrenome)
# # print(p1.idade)
# p1.Saudacao()
# p1.acao('estudando Python')


'''
entre as multiplas coisas que podemos fazer com as classes, podemos usar dos métodos para salvar algum dado do objeto, seja uma execucação de algo ou não. veja
'''


class Camera:
    def __init__(self, marca, status=False):
        self.marca = marca
        self.status = status

    def filmar(self):
        if self.status:
            print(f'A {self.marca} já está filmando.')
            return
        print(f'A {self.marca} está filmando.')
        self.status = True

    def ask(self):
        ask = input('Deseja parar de filmar? (s/n): ')
        ask = ask.lower
        if ask in ['s', 'sim']:
            self.status = False
            return self.status

    def fotografar(self):
        if self.status:
            print(f'A {self.marca} não pode fotografar enquanto filma.')
            print()
            self.ask()
            if not self.status:
                print(f'A {self.marca} parou de filmar.')
            else:
                print(f'A {self.marca} continua filmando.')
                return
        print(f'A {self.marca} está fotografando.')


c1 = Camera('Sony')
c2 = Camera('Canon')
c1.filmar()
print(c1.status)
print(c2.status)
c1.filmar()
c1.fotografar()
'''
parece confuso, mas não é.

temos a area de atribuir o nome da camera.

temos o status que define se a camera está ou não filmando.

possuimos tambem o método interno que serve para alterar o status da camera. tratamos os dados para um eventual caso de Sim, SIM, S. Quaisquer coisas além disso não serão entendidas commo sim, portanto mantem o status original. É ainda possível determinar o mesmo esquema para o não (n, N, Não, NÃO, não), mas no momento meu foco não é tratar eventuais problemas nesse código, mas anotar novamente cada um dos elementos estudados.
'''
# atributos da classe

'''
É essencial ter em mente que a classe possui um escopo próprio, ou seja, atributos e elementos internos dela que podem ser acessados interno e externamente. Claro, para que esse acesso seja feito existe uma forma correta de se fazer.

vimos em vários exemplos acima que o acesso costuma ser feito atraves do (.) veja o exemplo da classe camera acima. O grande problema é que nem sempre ter esse acesso externo da classe é algo desejável, pois pode impossibilitar a execução correta do código, como gerar a possibilidade do usuário alterar algo que não deveria ser alterado.

por exemplo, no caso da classe camera, o usuário poderia alterar o status diretamente, sem passar pelos métodos que tratam esse status. para evitar isso, podemos criar atributos privados.

python não possui atributos privados de fato, mas podemos simular isso utilizando __ (dunder) antes do nome do atributo.

por convenção usamos em python o _ (underscore) para atributos protegidos e __ (dunder) para atributos privados.

outra forma de manter o dado protegido é usando o seguinte exemplo:

classe Pessoa:
    ano_atual = 2026
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = Pessoa.ano_atual 

        def get_ano_nascimento(self):
            return Pessoa.ano_atual - self.idade

    isso impossibilita que um usuário altere o ano atual fora do contexto da classe. 

    conversão dos dados contidos na classe para json:
    
    Para isso, além do esquema clássico do json que temos no python, para salvar os dados jogamos dentro de uma variável um exemplo.__dict__ que converte os dados da classe em um dicionário, que é o formato aceito pelo json.
            
'''
# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.


class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)


p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa('Anônima', 23)
p4 = Pessoa.criar_sem_nome(25)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
# print(Pessoa.ano)
# Pessoa.metodo_de_classe()

'''
property 
a property é um decorator que transforma um método (dentro da classe) em um
atributo (somente leitura) para o código cliente.
vamos ao exemplo

'''


class Carro:
    def __init__(self, modelo, velocidade_maxima, cor):
        self.modelo = modelo
        self.tonalidade = cor
        self.velocidade_maxima = velocidade_maxima

    @property
    def cor(self):
        return self.tonalidade


c1 = Carro('Fusca', 120, 'Azul')
print(c1.cor)

# c1.cor = 'vermelho'  # AttributeError: can't set attribute
'''
note que ao tentar alterar a cor do carro, recebemos um erro, pois o atributo cor é somente leitura.
isso é útil quando queremos expor um atributo para o código cliente, mas não queremos que ele seja alterado diretamente.
'''
'''
no getter e no setter o que fazemos é criar métodos que vão quase se comportar como atributos, mas com a diferença que podemos controlar o acesso a esses atributos.

para melhorar a compreensão.

ao criar a instancia da classe, podemos passar o valor do atributo diretamente, mas ao tentar acessar esse atributo, na verdade estamos chamando o método getter. e ao tentar alterar o valor do atributo, estamos chamando o método setter. Isso permite alterarmos um nome dentro da nossa classe sem quebrar o código cliente que utiliza essa classe. Mas nos permite tratar, controlar e limitar uma alteração de valor.

vamos ao exemplo:
'''


class Caneta:
    def __init__(self, cor):
        self._cor = cor  # atributo protegido

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, nova_cor):
        if nova_cor not in ['azul', 'vermelho', 'verde']:
            print('Cor inválida!')
            return
        self._cor = nova_cor


caneta1 = Caneta('azul')
print(caneta1.cor)  # azul
caneta1.cor = 'amarelo'  # Cor inválida!
print(caneta1.cor)  # azul
caneta1.cor = 'vermelho'
print(caneta1.cor)  # vermelho

'''
Quando falamos de progromação orientada a objetos temos 4 pilares principais:
1. Abstração
2. Encapsulamento
3. Herança
4. Polimorfismo

no encapsulamento temos:
associação
agregação
composição

'''


class Mecanico:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class Ferramenta:
    def __init__(self, nome):
        self.nome = nome

    def usar_ferramenta(self):
        return f'usando a ferramenta {self.nome}.'


ferramenta1 = Ferramenta('Chave de fenda')
mecanico1 = Mecanico('Carlos')
mecanico1.ferramenta = ferramenta1
print(
    f' O mecânico {mecanico1.nome} está {mecanico1.ferramenta.usar_ferramenta()}.')
