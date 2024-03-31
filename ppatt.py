from datetime import date

escolha = 0
addhist = []
nome = []
cpf = []
numeroconta = []
saldolista = []
historicodepositos = []
historicocompras = []

def traco(x = 50):
    for i in range(0, x):
        print("=", end='')
    print("\n")

def historicodep(pre):
    deposito = [nome[0],pre,date.today()]

    historicodepositos[0].append(deposito)


def historico(pre,des):
    compras = [nome[0],pre,des,date.today()]

    historicocompras[0].append(compras)

def trocar_posicoes(lista, pos1, pos2):
    lista[pos1], lista[pos2] = lista[pos2], lista[pos1]
    return lista

def menuinicial():
    traco()
    print("Crie uma conta para iniciar o sistema:")
    print("1-Cadastrar")
    
    escolha = int(input('Escolha um número pra navegar:'))
    traco()

    if escolha == 1:
        cadastroinicial()

    else:
        print('digite um número que tenha nas opções')
        menuinicial()

def menu():
    traco()
    print('Bem vindo', nome[0],'!\n')
    print('Digite o número indicado para navegar:\n')
    print('1-Adicionar nova conta\n',
        '2-Conta\n',
        '3-Pix\n',
        '4-Depositar\n',
        '5-Extrato\n')
    escolha = int(input('Escolha um número pra navegar:'))
    traco()

    if escolha == 1:
        cadastro()

    elif escolha == 2:
        conta()
    
    elif escolha == 3:
        pix()
    
    elif escolha == 4:
        depositar()
    
    elif escolha == 5:
        extrato()
    
    else:
        print('digite um número que tenha nas opções')
        menu()
        
def cadastroinicial():
    traco()
    print('CADASTRO:\n',
            '1-Adicionar conta')
    escolha = int(input('Escolha um número pra navegar:'))
    traco()

    if escolha == 1:
        traco()
        name = input('Nome:')
        cpfa = input('CPF:')
        numeroc = input('Número da conta:')
        traco()

        saldolista.append(0)
        nome.append(name)
        cpf.append(cpfa)
        numeroconta.append(numeroc)
        historicocompras.append(addhist)
        menu()
    
    else:
        print('error!!!')
        menuinicial()

def cadastro():
    traco()
    print('ADD conta:\n',
            '1-Adicionar conta\n',
            '2-Voltar\n')
    escolha = int(input('Escolha um número pra navegar:'))
    traco()

    if escolha == 1:
        traco()
        name = input('Nome:')
        cpfa = input('CPF:')
        numeroc = input('Número da conta:')
        traco()

        saldolista.append(0)
        nome.append(name)
        cpf.append(cpfa)
        numeroconta.append(numeroc)
        historicocompras.append(addhist)

        menu()
    elif escolha ==2:
        #voltar pro menu
        menu()
    
    else:
        print('error!!!')
        menu()

def conta():
    traco()
    print('CONTA:\n',
        '1-Saldo\n',
        '2-Excluir conta\n',
        '3-Mudar de conta\n',
        '4-Alterar conta\n',
        '5-Informações da conta\n',
        '6-Voltar\n')
    escolha = int(input('Escolha um número pra navegar:'))
    traco()

    if escolha == 1:
        traco()
        print('Seu saldo atual: R$:', saldolista[0], "\n")
        print('1-Voltar')

        escolha = int(input('Escolha um número pra navegar:'))
        traco()
        
        if escolha == 1:
            conta()
        else:
            print('erro!')
            menu()
    elif escolha == 2:
        traco()
        print('Você tem certeza que deseja excluir uma conta?\n')
        print('1-SIM\n',
            '2-NÃO')

        escolha = int(input('Escolha um número pra navegar:'))
        traco()

        if escolha == 1:
            traco()
            excluircpf = input("digite o cpf da conta que deseja excluir:")

            posicaolista = cpf.index(excluircpf)
            del nome[posicaolista]
            del numeroconta[posicaolista]
            del saldolista[posicaolista]
            del historicocompras[posicaolista]
            del cpf[posicaolista]

            print('conta exluida!')
            traco()

            conta()

        elif escolha == 2:
            conta()

        else:
            print('error!!!')
            conta()

    elif escolha == 3:
        traco()
        alterarconta = input('Digite o cpf da conta que você deseja usar:')

        posicaolista = cpf.index(alterarconta)
        trocar_posicoes(nome,0,posicaolista)
        trocar_posicoes(numeroconta,0,posicaolista)
        trocar_posicoes(saldolista,0,posicaolista)
        trocar_posicoes(historicocompras,0,posicaolista)
        trocar_posicoes(cpf,0,posicaolista)

        print('Conta trocada com sucesso!')
        traco()

        menu()

    elif escolha == 4:
        traco()
        localconta = input('Digite o CPF da conta que deseja alterar:')

        indexconta = cpf.index(localconta)

        print('Alterar conta:\n',
            'Escolha a opcção que deseja alterar:\n',
            '1-Nome\n',
            '2-CPF\n',
            '3-Voltar')
        
        escolha = int(input('Escolha um número pra navegar:'))
        traco()

        if escolha == 1:
            novonome = input('digite o novo nome:')

            nome[indexconta] = novonome
            print('Nome alterado com sucesso!')
            traco()
            conta()
        
        elif escolha == 2:
            novocpf = input('digite o novo CPF:')

            cpf[indexconta] = novocpf
            print('CPF alterado com sucesso!')
            traco()
            conta()
        
        else:
            print('ERRO!')
            conta()
    
    elif escolha == 5:
        traco()
        print('Info:\n',
            'Nome:',nome[0],'\n',
            'CPF:',cpf[0],'\n',
            'Número da conta:',numeroconta[0],'\n',
            'Saldo:',saldolista[0],'\n\n',
            '1-Voltar')
        
        escolha = int(input('Escolha um número pra navegar:'))

        if escolha == 1:
            conta()
        
        else:
            print("ERROR!")
            conta()

    elif escolha == 6:
        #voltar
        menu()
    else:
        print('error!!!')
        conta()

def pix():
    traco()
    print('PIX:\n',
        'Saldo atual: R$', saldolista[0], '\n',
        '1-Realizar compra\n',
        '2-Voltar\n')
    escolha = int(input('Escolha um número pra navegar:'))
    traco()

    if escolha == 1:
        traco()
        compra = float(input('Digite o preço da compra:'))

        if saldolista[0] > compra:
            destinatario = input('Digite o nome do destinatério:')
            
            historico(compra,destinatario)

            saldolista[0] = saldolista[0] - compra

            

            print('Compra realizada! :D')
            traco()
            pix()
        
        elif saldolista[0] < compra:
            print('Saldo insufuciente para essa compra :(')
            traco()
            pix()

        
    elif escolha == 2:
        #Voltar
        menu()
    
    else:
        print('error!!!')
        menu()

def depositar():
    traco()
    print('DEPOSITO:\n',
       '1-Depositar em sua conta\n',
        '2-Voltar\n')
    escolha = int(input('Escolha um número pra navegar:'))
    traco()
    
    if escolha == 1:
        traco()
        deposito = float(input('Valor a ser depositado:'))
        saldolista[0] = saldolista[0] + deposito

        historicodep(deposito)

        print('Valor depositado! :D\n')
        print('1-Voltar')

        escolha = int(input('Escolha um número pra navegar:'))
        traco()

        if escolha == 1:
            depositar()
        
        else:
            print('erro!')
            menu()

    elif escolha == 2:
        #Voltar
        menu()
    
    else:
        print('error!!!')
        menu()

def extrato():
    traco()
    print('EXTRATO:\n',
        '1-Histórico de compras\n',
        '2-Histórico de depositos\n',
        '3-Voltar\n')
    escolha = int(input('Escolha um número pra navegar:'))
    traco()

    if escolha == 1:
        print('HISTÓRICO(COMPRAS):\n')
        traco()
        
        for y in range(len(historicocompras[0])):
            print('--nome:',historicocompras[0][y][0],'--Preço:R$',historicocompras[0][y][1],'--destinatário:',historicocompras[0][y][2],'--data:',historicocompras[0][y][3])
        
        print('1-Voltar')
        
        escolha = int(input('Escolha um número pra navegar:'))
        traco()

        if escolha == 1:
            extrato()
        else:
            print('error!!!')
            extrato()

    elif escolha == 2:
        traco()
        print('HISTÓRICO(DEPOSITOS):\n')
        
        for y in range(len(historicodepositos[0])):
            print('--nome:',historicodepositos[0][y][0],'--Preço depositado:R$',historicodepositos[0][y][1])
        print('1-Voltar')
        traco()

        escolha = int(input('Escolha um número pra navegar:'))

        if escolha == 1:
            extrato()
        else:
            print('error!!!')
            menu()
    elif escolha == 3:
        #volta
        menu()
    else:
        print('error!!!')
        menu()

menuinicial()