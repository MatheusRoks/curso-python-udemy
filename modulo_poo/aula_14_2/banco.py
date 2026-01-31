from registro import RegistroJson
from contas import ContaCorrente, ContaPoupanca
from clientes import Cliente


class Banco:
    def __init__(self, registro: RegistroJson):
        self._registro = registro
        self._clientes = []
        self._contas = []
        self._agencias = set()

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

    def autenticar(self, cliente, conta):
        return (
            self.checar_agencia(conta.agencia)
            and self.checar_cliente(cliente)
            and conta in cliente._contas
            and self.checar_conta(conta)
        )

    def salvar(self):
        self._registro.salvar_banco(self._clientes)

    def realizar_saque(self, cliente, conta, valor):

        if self.autenticar(cliente, conta):
            if conta.saque(valor):
                self.salvar()
                return True
        return False

    def realizar_deposito(self, cliente, conta, valor):

        if self.autenticar(cliente, conta):
            if conta.depositar(valor):
                self.salvar()
                return True
        return False

    def carregar(self):
        dados = self._registro.carregar_banco()
        self._clientes.clear()
        self._contas.clear()
        self._agencias.clear()

        for cliente_dict in dados:
            cliente = Cliente(
                cliente_dict['nome'],
                cliente_dict['idade'],
                cliente_dict['cpf']
            )
            self.adicionar_cliente(cliente)

            for conta_dict in cliente_dict['contas']:
                conta = self._criar_conta_por_dict(conta_dict)
                self.adicionar_conta(conta)
                cliente.adicionar_conta(conta)
                self.adicionar_agencia(conta.agencia)

    def _criar_conta_por_dict(self, dados):
        if dados['Tipo'] == 'ContaCorrente':
            return ContaCorrente(
                dados['Agência'],
                dados['Número'],
                dados['Saldo'],
                dados['Limite']
            )

        if dados['Tipo'] == 'ContaPoupanca':
            return ContaPoupanca(
                dados['Agência'],
                dados['Número'],
                dados['Saldo']
            )

        raise ValueError('Tipo de conta inválido')
