from contextlib import contextmanager


@contextmanager
def abrir_arquivo(caminho_arquivo, modo, encoding='utf-8'):
    print(f"Abrindo o arquivo {caminho_arquivo} no modo '{modo}'")
    arquivo = open(caminho_arquivo, modo)
    try:
        yield arquivo
    finally:
        print(f"Fechando o arquivo {caminho_arquivo}")
        arquivo.close()


with abrir_arquivo('aula09.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
