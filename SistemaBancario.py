menu = '''
    -------------- SISTEMA BANCÁRIO --------------
    [1] - Depositar 
    [2] - Sacar
    [3] - Extrato
    [4] - Sair
    ----------------------------------------------
    Digite a opção desejada:  
'''
saldo_cliente = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

# Programa Principal
while True:

    escolha = int(input(menu))
    while (escolha <= 0 or escolha > 4):
        print('Você digitou um número inválido. Digite novamente.')
        escolha = int(input(menu))

    # Operação para realizar depósito
    if (escolha == 1):
        valor_deposito = float(input('Digite o valor que deseja depositar: R$'))
        while (valor_deposito <= 0):
            print('Você digitou um valor negativo.')
            valor_deposito = float(input('Digite novamente o valor que deseja depositar: R$'))
        else:
            saldo_cliente += valor_deposito
            extrato+= (f"Depósito realizado no valor de R${valor_deposito}\n")
            print(f'Você depositou R${valor_deposito}')

    
    # Operação para sacar        
    elif (escolha == 2):               
        sacar = float(input('Quanto deseja sacar ? R$ '))
        if numero_saque == LIMITE_SAQUE:
            print("""
            Gostaríamos de informar que o limite diário de saque em sua conta foi atingido. 
            O número máximo de saques permitidos por dia é de 3 vezes, e esse limite já foi 
            alcançado em sua conta.
            """)
        else:    
            while (sacar > limite):
                print('Valor inválido, seu limite é de R$500.00 por saque.')
                sacar = float(input('Quanto deseja sacar ? R$ '))
            while (sacar > saldo_cliente) or (sacar <= 0):
                print('Valor inválido, digite novamente.')
                sacar = float(input('Quanto deseja sacar ? R$ '))
            saldo_cliente-=sacar
            numero_saque+=1
            extrato+= (f"Saque realizado no valor de R${sacar}\n")
            print(f'Você sacou R${sacar}')
      
    # Operação para vizualizar o extrato
    elif (escolha == 3):
        print(extrato)
        print(f"Seu saldo atual é de R${saldo_cliente}")

     # Operação para sair do sistema
    elif (escolha == 4):
        print('Você foi desconectado do sistema. Volte sempre!')
        break


          