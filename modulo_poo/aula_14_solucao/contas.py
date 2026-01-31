import json
from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor: float):
        ...

    def depositar(self, valor: float) -> float:
        if valor <= 0:
            raise ValueError(f'O valor do depósito não pode ser {valor}')
        self.saldo += valor
        return self.saldo

    def to_dict(self) -> dict:
        return {
            'Tipo': self.__class__.__name__,
            'Agência': self.agencia,
            'Conta': self.conta,
            'Saldo': self.saldo,
        }


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> bool:
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            return True
        return False


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float, limite:
                 float = 500):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> bool:
        new_saldo = self.saldo + self.limite
        valor_pos_saque = self.saldo - valor

        if valor > self.saldo and valor <= new_saldo:
            self.limite -= (valor - self.saldo)
            self.saldo = 0
            return True
        elif valor_pos_saque >= 0:
            self.saldo -= valor
            return True
        else:
            return False

    def to_dict(self) -> dict:
        dict_conta = super().to_dict()
        dict_conta.update({'Limite': self.limite})
        return dict_conta
