from abc import ABC


class Pessoa(ABC):
    def __init__(self, nome: str, idade: int, cpf: str | int):
        self._nome = nome
        self._idade = idade
        self._cpf = cpf
