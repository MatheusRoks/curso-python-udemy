import json
import os

pessoas = [
    {"nome": 'Ana', "idade": 20},
    {"nome": 'Bia', "idade": 25},
    {"nome": 'Carlos', "idade": 30}
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_ARQUIVO = os.path.join(BASE_DIR, 'pessoas.json')

with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    json.dump(pessoas, arquivo, indent=2)
