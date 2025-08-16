dicio1= {
    'nome': 'João',
    'idade': 20,
    'altura': 1.75
}
dicio2 = {
    'mãe': 'Maria',
    'media': 7,}

dicio3 = {**dicio1, **dicio2}
print(dicio3)    

def exibe_argumentos(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

exibe_argumentos(nome='João', idade=20,)

#basicamente, kwargs é um dicionário que recebe os argumentos nomeados passados para a função. A função exibe_argumentos percorre esse dicionário e imprime cada chave e valor formatados. Isso é útil quando você quer passar um número variável de argumentos nomeados para uma função e processá-los de maneira flexível.

exibe_argumentos(**dicio3)