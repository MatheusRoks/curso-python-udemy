'''
aqui vem a forma 'complexa' de se fazer uma classe de erro
'''


class MyError(Exception):
    ...


class MyOtherError(Exception):
    ...


def levantar():
    ex = MyError('um erro qualquer')
    ex.add_note('Tudo certo por aqui, só testando o role')
    raise ex


try:
    levantar()
except MyError as e:
    print(e)
    another = MyOtherError('outro erro qualquer')
    raise another from e
