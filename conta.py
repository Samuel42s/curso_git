saldo = 0

while True:
    print("\n1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f'Depósito de R${valor_deposito:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser maior que zero.')

    elif opcao == '2':
        valor_saque = float(input("Digite o valor do saque: "))
        if valor_saque <= saldo:
            print(f'Parabéns, seu saque no valor de {valor_saque} foi aprovado!')
        else:
            print(f'Seu saldo no valor de {valor_saque} foi negado! Você não possui saldo suficiente!')
        # -----------------------------------------
        # Desenvolva a lógica da validação do saldo
        # -----------------------------------------

    elif opcao == '3':
        print(f'\nExtrato bancário:')
        print(f'Saldo atual: R${saldo:.2f}')

    elif opcao == '4':
        print("Saindo...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
