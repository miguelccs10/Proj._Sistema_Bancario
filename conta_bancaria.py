menu = """
======================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
======================
=> """

saldo = 0
limite = 500
extrato = ""
num_saques = 0
LIMITE_SAQUES = 3


def _deposito(valor):
    global saldo, extrato

    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print(f"\nDeposito de R${valor} realizado com sucesso!")
    
    else:
        print("\nO valor informado é invalido!")

def _sacar(valor):
    global saldo, extrato, num_saques
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = num_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("\nVocê nâo tem saldo suficiente!")
    elif excedeu_limite:
        print("\nO valor que deseja sacar é maior que o limite de R$500 diario!")
    elif excedeu_saque:
        print("\nNumero maximo de saques excedido!")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        num_saques += 1
        print(f"\nSaque de R${valor} realizado com sucesso!")
    else:
        print("\nValor informado invalido!")

def _extrato():
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

while True:
    try:
        opcao = input(menu)

        operacoes = {
            "d": lambda: _deposito(float(input("Informe o valor de deposito: "))),
            "s": lambda: _sacar(float(input("Informe o valor de saque: "))),
            "e": lambda: _extrato(),
            "q": lambda: exit("\nObrigado por usar nossos serviços, volte sempre <3")
        }

        operacoes[opcao]()
        
    except ValueError:
        print("Operação invalida! Por favor, selecione novamente a opção desejada.")