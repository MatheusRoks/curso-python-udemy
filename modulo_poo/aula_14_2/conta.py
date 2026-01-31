from abc import ABC, abstractmethod
from registro import RegistroArquivoMixin


class Conta(RegistroArquivoMixin):
    def __init__(self, agencia: int, numero: int, saldo: float = 0):
        self._agencia = agencia
        self._numero = numero
        self._saldo = saldo

    @abstractmethod
    def saque(self, valor: float) -> bool:
        pass

    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            self.registrar_erro(f'Depósito de valor inválido: {valor}.')
            return False
        self._saldo += valor
        self.registrar_deposito(f'Depósito de {valor} realizado com sucesso.')
        return True

    def ver_saldo(self) -> float:
        return self._saldo

    @property
    def agencia(self):
        return self._agencia

    def to_dict(self) -> dict:
        return {
            'Tipo': self.__class__.__name__,
            'Agência': self._agencia,
            'Número': self._numero,
            'Saldo': self._saldo,
            'Limite': getattr(self, '_limite', None)

        }
