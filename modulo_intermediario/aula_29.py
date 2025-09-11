from itertools import groupby

alunos = [
    {'nome': "paulo",
     'nota': 'A'},
    {'nome': "maria",
     'nota': 'C'},
    {'nome': "édro",
     'nota': 'B'},
    {'nome': "matheus",
     'nota': 'A'},
    {'nome': "manoel",
     'nota': 'A'},
]


def ordena(aluno):
    return aluno['nota']


ordenado = sorted(alunos, key=ordena)

agrupado = groupby(ordenado, key=ordena)

for chave, grupo in agrupado:
    print(chave)
    for aluno in grupo:
        print(aluno)
