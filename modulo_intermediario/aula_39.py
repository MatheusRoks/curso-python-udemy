import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_ARQUIVO = os.path.join(BASE_DIR, 'pessoa.json')


class Person:
    def __init__(self, name, age, city=None, job=None):
        self.name = name
        self.age = age
        self.city = city
        self.job = job


valor = True

while valor:
    name = input('Digite seu nome: ')
    age = input('Digite sua idade: ')
    city = input('Digite sua cidade: ')
    job = input('Digite sua profissão: ')
    p1 = Person(name, age, city, job)
    valor = False

pd = [p1.__dict__]
with open(CAMINHO_ARQUIVO, "w", encoding='utf-8') as arquivo:
    json.dump(pd, arquivo, indent=2)

with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Person(**pessoas[0])
