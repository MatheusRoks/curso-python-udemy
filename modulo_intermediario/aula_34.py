# Leia também: https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/
# with open (context manager) e métodos úteis do TextIOWrapper
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load


caminho_arquivo = r"C:\\Users\\Usuário\\Desktop\\~\\repositories\curso-python-udemy\\"
caminho_arquivo += 'testando.txt'

with open(caminho_arquivo, "w+", encoding='utf8') as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")
    arquivo.write("Linha 3\n")
    arquivo.write("Linha 4\n")
    arquivo.write("Linha 5\n")
    arquivo.write("Linha 6\n")
    arquivo.write("Linha 7\n")
    arquivo.write("Linha 8\n")
    arquivo.write("Linha 9\n")
    arquivo.write("Linha 10\n")
    print("Arquivo criado com sucesso!")
    print('lendo o arquivo:')
    arquivo.seek(0, 0)
    print(arquivo.read())

print('#' * 20)
with open(caminho_arquivo, "r") as arquivo:
    print(arquivo.read())
