menu = """

[1] Depósito
[2] Saque
[3] Extrato
[4] Sair 

==> """

saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUE = 3
numero_saques = 0


while True:

    opcao = input(menu)

    if opcao == '1':
        valor = float(input("Informe o valor que será depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("O valor informado é inválido.")

    elif opcao == '2':
        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Você não possui saldo suficiente em conta.")

        elif excedeu_limite:
            print("O valor de saque ultrapassa o limite diário.")

        elif excedeu_saques:
            print("Você ultrapassou o limite diário de saques.")
            print(f'Total de saques {numero_saques}')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque no valor de R$ {valor:.2f}\n'
            numero_saques += 1

        else:
            print('O valor informado é inválido.')

    elif opcao == '3':
        print("\nExtrato\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')

    elif opcao == '4':
        break
    else:
        print("Opção inválida. Favor selecione a opção desejada.")
