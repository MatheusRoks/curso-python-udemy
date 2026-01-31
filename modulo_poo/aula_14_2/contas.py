from conta import Conta
from registro import RegistroArquivoMixin


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float = 0.0, limite:
                 float = 1000.0):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    def saque(self, valor: float) -> bool:
        if valor > (self._saldo + self._limite):
            self.registrar_erro(
                f'Saque de {valor} excede o limite disponível.')
            return False
        self._saldo -= valor
        self.registrar_saque(f'Saque de {valor} realizado com sucesso.')
        return True


class ContaPoupanca(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float = 0.0):
        super().__init__(agencia, conta, saldo)

    def saque(self, valor: float) -> bool:
        if valor > self._saldo:
            self.registrar_erro(
                f'Saque de {valor} excede o saldo disponível.'
            )
            return False
        self._saldo -= valor
        self.registrar_saque(f'Saque de {valor} realizado com sucesso.')
        return True
