from pessoa import Pessoa
from contas import ContaCorrente, ContaPoupanca


class Cliente(Pessoa):
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade, cpf)
        self._contas = []

    def adicionar_conta(self, conta: ContaCorrente | ContaPoupanca):
        self._contas.append(conta)

    def listar_contas(self):
        return [conta.to_dict() for conta in self._contas]

    def to_dict(self):
        return {
            'nome': self._nome,
            'idade': self._idade,
            'cpf': self._cpf,
            'contas': self.listar_contas()
        }
