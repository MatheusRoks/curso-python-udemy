from registro import RegistroJson, CAMINHO_ARQUIVO
from contas import Banco, Cliente, ContaCorrente, ContaPoupanca


def executar_teste():
    persistencia = RegistroJson(CAMINHO_ARQUIVO)
    banco = Banco(persistencia)

    banco.adicionar_agencia(1111)
    banco.adicionar_agencia(2222)

    cliente1 = Cliente("Thiago", 30, "111.222.333-44")
    cc_thiago = ContaCorrente(1111, 5050, 100, 1000)
    cliente1.adicionar_conta(cc_thiago)

    cliente2 = Cliente("Maria", 25, "555.666.777-88")
    cp_maria = ContaPoupanca(2222, 8080, 200)
    cliente2.adicionar_conta(cp_maria)

    banco.adicionar_cliente(cliente1)
    banco.adicionar_conta(cc_thiago)

    banco.adicionar_cliente(cliente2)
    banco.adicionar_conta(cp_maria)

    print("-" * 30)
    print("INICIANDO TESTES DE SAQUE")
    print("-" * 30)

    print(f"Cliente: {cliente1._nome} | Saldo Inicial: {cc_thiago._saldo}")
    if banco.autenticar(cliente1, cc_thiago):
        if cc_thiago.saque(500):
            print(f" Saque de R$500 OK! Saldo Atual: {cc_thiago._saldo}")
        else:
            print(" Saque negado.")

    if cc_thiago.saque(2000):
        print(" Saque OK!")
    else:
        print(f" Saque de R$2000 negado (Limite insuficiente).")

    print(f"\nCliente: {cliente2._nome} | Saldo Inicial: {cp_maria._saldo}")
    try:
        if banco.autenticar(cliente2, cp_maria):
            cp_maria.saque(300)
    except ValueError as e:
        print(f" Erro na Poupança: {e}")

    persistencia.salvar_banco(banco._clientes)
    print("\n" + "="*30)
    print("ESTADO FINAL SALVO NO JSON COM SUCESSO!")
    print("="*30)


if __name__ == "__main__":
    executar_teste()
