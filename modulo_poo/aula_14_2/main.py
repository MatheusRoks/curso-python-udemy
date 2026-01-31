from registro import RegistroJson, CAMINHO_ARQUIVO
from banco import Banco
from clientes import Cliente
from contas import ContaCorrente, ContaPoupanca


def main():
    registro = RegistroJson(CAMINHO_ARQUIVO)
    banco = Banco(registro)

    # cria agência
    banco.adicionar_agencia(1)

    # cria cliente
    cliente = Cliente("João", 30, "12345678900")
    banco.adicionar_cliente(cliente)

    # cria contas (BANCO é dono)
    cc = ContaCorrente(agencia=1, conta=1001, saldo=0, limite=1000)
    cp = ContaPoupanca(agencia=1, conta=2001, saldo=500)

    banco.adicionar_conta(cc)
    banco.adicionar_conta(cp)

    # banco empresta contas ao cliente
    cliente.adicionar_conta(cc)
    cliente.adicionar_conta(cp)

    # operações
    banco.realizar_deposito(cliente, cc, 300)
    banco.realizar_saque(cliente, cc, 200)
    banco.realizar_saque(cliente, cp, 100)

    print("ANTES DE SALVAR:")
    print(cliente.to_dict())

    banco.salvar()

    # simula reinício do sistema
    banco2 = Banco(registro)
    banco2.carregar()

    print("\nDEPOIS DE RECARREGAR DO JSON:")
    for c in banco2._clientes:
        print(c.to_dict())


if __name__ == "__main__":
    main()
