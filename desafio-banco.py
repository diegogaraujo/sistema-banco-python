menu = """

[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] SAIR

=>  """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    #depositar
    if opcao == "1":

        valor = float(input("Informe valor para deposito: R$ "))

        if valor > 0 :
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido.")

    #sacar            
    elif opcao == "2":

        valor = float(input("Informe valor para saque: R$ "))
                    
        if saldo > 0 and limite >= valor > 0 and numero_saques < LIMITE_SAQUES :
            saldo = saldo - valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
        elif saldo <= 0 :
                print("Saldo insuficiente!")
        elif valor <= 0 :
            print("Valor inválido!")
        elif numero_saques >= LIMITE_SAQUES :
            print("Limite de saques excedido!")
        elif valor > limite:
            print("Limite por saque R$ 500,00")

    #extrato
    elif opcao == "3":
        print("============ Extrato =============")
        print(extrato)
        print(f"Total em conta: R$ {saldo:.2f}")
        print("===================================")
        
    #sair
    elif opcao == "4":
        break

    #opcão inválida
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")