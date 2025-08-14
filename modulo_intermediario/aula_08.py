#shallow copy e deep copy   

'''
a copia rasa, shallow copy, é feita quando se copia um objeto para outro objeto, mas não os objetos internos.
o que isso significa? basicamente, ao eu utilizar o metodo copy() em um dicionário
eu crio um novo dicionário com as mesmas chaves e valores, porem
se o valor for um objeto mutável, como uma lista ou outro dicionário,
o novo dicionário terá uma referência ao mesmo objeto, ou seja, se eu alterar o objeto interno
no novo dicionário, o objeto interno do dicionário original também será alterado.
por essa razão, ela é chamada de copia rasa.

mas podemos utilizar do modulo copy para fazer uma copia profunda, deep copy.
a copia profunda, deep copy, é feita quando se copia um objeto e todos os objetos internos.
isso significa que, ao utilizar o metodo deepcopy() do modulo copy,
vamos ao exemplo

'''

import copy

dicionario = {
    'nome': 'João',
    'idade': 30,
    'enderecos': {
        'casa': 'Rua A, 123',
        'trabalho': 'Avenida B, 456'
    },
    "l1": [1, 2, 3],
}
print("Dicionário Original:", dicionario)
dicionario_copia_rasa = dicionario.copy()
dicionario_copia_profunda = copy.deepcopy(dicionario)
dicionario_copia_rasa['enderecos']['casa'] = 'Rua C, 789'
dicionario_copia_profunda['enderecos']['casa'] = 'Rua D, 1011'
print("Dicionário Original:", dicionario)
print("Cópia Rasa:", dicionario_copia_rasa)
print("Cópia Profunda:", dicionario_copia_profunda)

