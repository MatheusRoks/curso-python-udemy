from abc import ABC, abstractmethod
import registro


class Banco:
    def __init__(self, persistencia: registro.RegistroJson):
        self._clientes = []
        self._contas = []
        self._agencias = set()
        self._persistencia = persistencia

    def adicionar_agencia(self, agencia):
        self._agencias.add(agencia)

    def adicionar_cliente(self, cliente: 'Cliente'):
        self._clientes.append(cliente)

    def adicionar_conta(self, conta: 'Conta'):
        self._contas.append(conta)

    def checar_agencia(self, agencia):
        return agencia in self._agencias

    def checar_cliente(self, cliente):
        return cliente in self._clientes

    def checar_conta(self, conta):
        return conta in self._contas

    def autenticar(self, cliente: 'Cliente', conta: 'Conta') -> bool:
        agencia_valida = self.checar_agencia(conta._agencia)
        cliente_valido = self.checar_cliente(cliente)
        conta_valida = self.checar_conta(conta)
        if agencia_valida and cliente_valido and conta_valida:
            return True
        return False

    def salvar(self):

        self._persistencia.salvar_banco(self._clientes)

    def realizar_saque(self, cliente, conta, valor):

        if self.autenticar(cliente, conta):
            if conta.saque(valor):
                self.salvar()
                return True
        return False


@abstractmethod
class Conta(ABC):
    def __init__(self, agencia: int, numero: int, saldo: float = 0):
        self._agencia = agencia
        self._numero = numero
        self._saldo = saldo

    def saque(self, valor) -> bool:
        ...

    def deposito(self, valor):
        self._saldo += valor

    def to_dict(self):
        return {
            'tipo': self.__class__.__name__,
            'agencia': self._agencia,
            'numero': self._numero,
            'saldo': self._saldo,
            'limite': getattr(self, '_limite', None)
        }


class ContaCorrente(Conta, registro.RegistroFileMixin):
    def __init__(self, agencia: int, numero: int, saldo: float = 0, limite=1000):
        super().__init__(agencia, numero, saldo)
        self._limite = limite

    def saque(self, valor) -> bool:
        if valor > (self._saldo + self._limite):
            return False
        self._saldo -= valor
        self.registrar_saque(
            f'Valor do saque: {valor}. Saldo atual: {self._saldo}')
        return True


class ContaPoupanca(Conta, registro.RegistroFileMixin):
    def __init__(self, agencia: int, numero: int, saldo: float = 0):
        super().__init__(agencia, numero, saldo)

    def saque(self, valor) -> bool:
        if valor <= self._saldo:
            self._saldo -= valor
            self.registrar_saque(
                f'Valor do saque: {valor}. Saldo atual: {self._saldo}')
            return True
        raise ValueError("Saldo insuficiente.")


@abstractmethod
class Pessoa(ABC):
    def __init__(self, nome: str, idade: int, cpf: str):
        self._nome = nome
        self._idade = idade
        self._cpf = cpf


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, cpf: str):
        super().__init__(nome, idade, cpf)
        self._cpf = cpf
        self._contas = []

    def adicionar_conta(self, conta: Conta):
        self._contas.append(conta)

    def listar_contas(self):
        return [conta.to_dict() for conta in self._contas]

    def to_dict(self):
        return {
            'tipo': self.__class__.__name__,
            'nome': self._nome,
            'idade': self._idade,
            'cpf': self._cpf,
            'contas': self.listar_contas()
        }
