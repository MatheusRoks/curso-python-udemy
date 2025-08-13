def saudar (saudacao, name):
    def saudacao_completa():
        return f"{saudacao}, {name}!"
    return saudacao_completa

saudacao_ola = saudar("Olá", "Maria")
saudacao_bem_vindo = saudar("Bem-vindo", "João")
print(saudacao_ola())  # Saída: Olá, Maria!
print(saudacao_bem_vindo())  # Saída: Bem-vindo, João!

'''
vamos explicar aqui o que esta acontecendo:
1. A função `saudar` recebe dois parâmetros: `saudacao` e `name`.
2. Dentro de `saudar`, definimos uma função interna chamada `saudacao_completa` que retorna uma string formatada com a saudação e o nome.
3. A função `saudar` retorna a função interna `saudacao_completa`, permitindo que ela seja chamada posteriormente, ou seja, ela é uma função de ordem superior. Ela permite
que você crie saudações personalizadas sem precisar definir uma nova função para cada saudação.
4. Criamos duas variáveis, `saudacao_ola` e `saudacao_bem_vindo`, que armazenam as funções retornadas por `saudar`.
5. Finalmente, chamamos essas funções para imprimir as saudações completas.

basicamente, estamos usando closures para criar funções personalizadas de saudação que podem ser reutilizadas. Isso é útil quando você precisa de uma função que depende de variáveis externas, como `saudacao` e `name`, mas não quer passar esses parâmetros toda vez que chama a função.

assim, o que da pra entender é:
quando definimos a primeira função, ela retorna uma função interna que "lembra" os valores dos parâmetros passados. Isso é o que chamamos de closure, onde a função interna tem acesso ao escopo da função externa mesmo depois que a função externa já foi executada.

isso altera o fluxo de execução do programa, pois agora temos funções que podem ser chamadas posteriormente, mantendo o contexto dos parâmetros passados. Isso é especialmente útil em programação funcional e quando queremos criar funções dinâmicas ou personalizadas.

assim, as funções que antes seriam imediatamente executadas agora podem ser chamadas quando necessário, permitindo uma maior flexibilidade e reutilização de código.

vamos ver um exemplo prático de como isso pode ser útil:
'''

def cumprimentar(saudacao):
    def cumprimentar_nome(name):
        return f"{saudacao}, {name}!"
    return cumprimentar_nome

cumprimentar_ola = cumprimentar("Olá")
cumprimentar_bom_dia = cumprimentar("Bom dia")
print(cumprimentar_ola("Ana"))  # Saída: Olá, Ana!
print(cumprimentar_bom_dia("Carlos"))  # Saída: Bom dia, Carlos!
'''
Nesse exemplo, a função `cumprimentar` cria funções de cumprimento personalizadas que podem ser reutilizadas com diferentes nomes. Isso demonstra como closures podem ser usadas para criar funções mais flexíveis e reutilizáveis.

vamos a mais exemplos
'''

nomes = ["Alice", "Bob", "Charlie"]
for nome in nomes:
    print(cumprimentar_ola(nome))