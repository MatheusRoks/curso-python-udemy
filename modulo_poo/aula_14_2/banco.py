from registro import RegistroJson
from contas import ContaCorrente, ContaPoupanca
from clientes import Cliente


class Banco:
    def __init__(self, registro: RegistroJson):
        self._registro = registro
        self._clientes = []
        self._contas = []
        self._agencias = set()

    @property
    def agencias(self):
        return self._agencias

    def adicionar_cliente(self, cliente: Cliente):
        self._clientes.append(cliente)

    def adicionar_conta(self, conta: ContaCorrente | ContaPoupanca):
        self._contas.append(conta)

    def adicionar_agencia(self, agencia: int):
        self._agencias.add(agencia)

    def checar_agencia(self, agencia: int) -> bool:
        return agencia in self._agencias

    def checar_cliente(self, cliente: Cliente) -> bool:
        return cliente in self._clientes

    def checar_conta(self, conta: ContaCorrente | ContaPoupanca) -> bool:
        return conta in self._contas

    def autenticar(self, cliente: Cliente, conta: ContaCorrente | ContaPoupanca) -> bool:
        agencia_valida = self.checar_agencia(conta.agencias)
        cliente_valido = self.checar_cliente(cliente)
        conta_valida = self.checar_conta(conta)
        if agencia_valida and cliente_valido and conta_valida:
            return True
        return False

    def salvar(self):
        self._registro.salvar_banco(self._clientes)
