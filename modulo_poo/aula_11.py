import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_ARQUIVO = os.path.join(BASE_DIR, 'lista_dicionario.json')


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."


p1 = Pessoa("Ana", 30)
dicionario_atributos = p1.__dict__

with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    json.dump(dicionario_atributos, arquivo, indent=2, ensure_ascii=False)

with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    dados_carregados = json.load(arquivo)


print(dados_carregados)
