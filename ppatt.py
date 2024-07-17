from datetime import datetime
from time import sleep

escolha = " "
addhist = []
nome = []
cpf = []
numeroconta = []
saldolista = []
historicodepositos = [[]]
historicocompras = [[]]

def traco(x = 50):
    for i in range(0, x):
        print("=", end='')
    print("\n")

def historicodep(pre):
    deposito = [nome[0],pre,datetime.now().hour]

    historicodepositos[0].append(deposito)


def historico(ind,pre,des):
    compras = [nome[ind],pre,des,datetime.now().hour]

    historicocompras[0].append(compras)

def trocar_posicoes(lista, pos1, pos2):
    lista[pos1], lista[pos2] = lista[pos2], lista[pos1]
    return lista

def menuinicial():
    traco()
    print("Crie uma conta para iniciar o sistema:")
    print("1-Cadastrar")
    traco()

    escolha = input('Escolha um número pra navegar:')

    if escolha == '1':
        cadastroinicial()

    else:
        print('digite um número que tenha nas opções')
        sleep(2)
        menuinicial()

def menu():
    traco()
    print('Conta atual:', nome[0],'\n')
    print('Digite o número indicado para navegar:\n')
    print('1-Adicionar nova conta\n',
        '2-Conta\n',
        '3-Transferência\n',
        '4-Depositar\n',
        '5-Extrato/Histórico\n')
    traco()
    escolha = input('Escolha um número pra navegar:')
    

    if escolha == '1':
        cadastro()

    elif escolha == '2':
        conta()
    
    elif escolha == '3':
        pix()
    
    elif escolha == '4':
        depositar()
    
    elif escolha == '5':
        extrato()
    
    else:
        print('digite um número que tenha nas opções')
        sleep(2)
        menu()
        
def cadastroinicial():
    traco()
    print('CADASTRO:\n',
            '1-Adicionar conta')
    traco()
    escolha = input('Escolha um número pra navegar:')
    

    if escolha == '1':
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
        historicodepositos.append(addhist)
        menu()
    
    else:
        print('digite um perfil válido!')
        sleep(2)
        menuinicial()

def cadastro():
    traco()
    print('ADD conta:\n',
            '1-Adicionar conta\n',
            '2-Voltar\n')
    traco()
    escolha = input('Escolha um número pra navegar:')
    

    if escolha == '1':
        traco()
        name = input('Nome:')
        cpfa = input('CPF(apenas números e 11 dígitos):')
        while len(cpfa) != 11:
            cpfa = input('CPF(apenas números e 11 dígitos):')
            print('digite um cpf válido(apenas números com 11 dígitos)')
            sleep(4)

        numeroc = input('Número da conta:')
        traco()

        saldolista.append(0)
        nome.append(name)
        cpf.append(cpfa)
        numeroconta.append(numeroc)
        historicocompras.append(addhist)
        historicodepositos.append(addhist)

        traco()
        print('Conta adicionada com sucesso! :D')
        sleep(3)
        cadastro()

    elif escolha == '2':
        #voltar pro menu
        menu()
    
    else:
        print('digite uma opção válido!')
        sleep(3)
        cadastro()

def conta():
    traco()
    print(f"{'CONTA':^40}")
    print(f"{nome[0]:^40}")
    traco()
    print('''
    1-Saldo
    2-Excluir conta
    3-Mudar de conta
    4-Alterar conta
    5-Informações da conta
    6-Voltar''')
    traco()
    escolha = input('Escolha um número pra navegar:')
    

    if escolha == '1':
        traco()
        print(f"{'SALDO':^40}")
        traco()
        print(f'\nSaldo atual de {nome[0]} : R$:', saldolista[0], "\n")
        print('1-Voltar')
        traco()

        escolha = input('Escolha um número pra navegar:')
        
        if escolha == '1':
            conta()
        else:
            print('escolha uma opção válida!(voltando para o menu de conta...)')
            sleep(4)
            conta()
    elif escolha == '2':
        traco()
        print('Você tem certeza que deseja excluir uma conta?\n')
        print('1-SIM\n',
            '2-NÃO')
        traco()

        escolha = input('Escolha um número pra navegar:')

        if escolha == '1':
            traco()
            excluircpf = input("digite o cpf da conta que deseja excluir:")

            posicaolista = cpf.index(excluircpf)

            print('Conta de:',nome[posicaolista],' exluida!\n')
            del nome[posicaolista]
            del numeroconta[posicaolista]
            del saldolista[posicaolista]
            del historicocompras[posicaolista]
            del historicodepositos[posicaolista]
            del cpf[posicaolista]

            if len(cpf) == 0:
                print('voltando para cadastro...')
                sleep(3)
                menuinicial()

            print('voltando para o menu conta...')
            sleep(3)
            conta()

        elif escolha == '2':
            conta()

        else:
            print('Ok, voltando para o menu conta...')
            sleep(3)
            conta()

    elif escolha == '3':
        traco()
        alterarconta = input('Digite o cpf da conta que você deseja usar:')

        posicaolista = cpf.index(alterarconta)
        trocar_posicoes(nome,0,posicaolista)
        trocar_posicoes(numeroconta,0,posicaolista)
        trocar_posicoes(saldolista,0,posicaolista)
        trocar_posicoes(historicocompras,0,posicaolista)
        trocar_posicoes(historicodepositos,0,posicaolista)
        trocar_posicoes(cpf,0,posicaolista)

        print('trocando conta...')
        sleep(2)
        print('Conta trocada com sucesso! voltando ao menu...')
        sleep(4)
        menu()

    elif escolha == '4':
        traco()
        localconta = input('Digite o CPF da conta que deseja alterar:')

        indexconta = cpf.index(localconta)
        traco()
        print(f'Alterando conta de {nome[indexconta]}:\n',
            'Escolha a opcção que deseja alterar:\n',
            '1-Nome\n',
            '2-CPF\n',
            '3-Voltar')
        traco()
        
        escolha = input('Escolha um número pra navegar:')

        if escolha == '1':
            novonome = input('digite o novo nome:')

            nome[indexconta] = novonome
            print('Nome alterado com sucesso! voltando ao menu conta')
            sleep(3)
            conta()
        
        elif escolha == '2':
            novocpf = input('digite o novo CPF:')

            cpf[indexconta] = novocpf
            print('CPF alterado com sucesso! voltando ao menu conta...')
            sleep(3)
            conta()
        
        else:
            print('digite uma opção válida! voltando ao menu conta...')
            sleep(3)
            conta()
    
    elif escolha == '5':
        traco()
        print('Info:\n',
            'Nome:',nome[0],'\n',
            'CPF:',cpf[0],'\n',
            'Número da conta:',numeroconta[0],'\n',
            'Saldo:',saldolista[0],'\n\n',
            '1-Voltar')
        traco()
        escolha = input('Escolha um número pra navegar:')

        if escolha == '1':
            conta()
        
        else:
            print("digite uma opção válida! voltando ao menu conta...")
            sleep(3)
            conta()

    elif escolha == '6':
        #voltar
        menu()
    else:
        print('digite uma opção válida! voltando ao menu conta...')
        sleep(3)
        conta()

def pix():
    traco()
    print(f"{'TRANFERÊNCIA':^40}")
    print(f"{'Saldo atual: R$':>20}{saldolista[0]}")
    print('''
    1-Realizar tranferência
    2-Voltar''')
    traco()
    escolha = input('Escolha um número pra navegar:')

    if escolha == '1':
        traco()
        compra = float(input('Digite o preço da transferência:'))

        if saldolista[0] > compra:
            destinatario = input('Digite o nome do destinatário:')
            cpfimg = input('Digite o cpf do destinatário:')

            if destinatario not in nome:
                print('essa conta não existe! voltando ao menu Tranferência...')
                sleep(3)
                pix()
            
            if cpfimg in cpf:
                destinatariosistema = nome.index(destinatario)
                saldolista[destinatariosistema] = saldolista[destinatariosistema] + compra
            else:
                print('Essa conta não existe! voltando ao menu tranferência...')
                sleep(3)
                pix()

            historico(compra,destinatario)

            trocar_posicoes(nome,0,destinatariosistema)
            trocar_posicoes(numeroconta,0,destinatariosistema)
            trocar_posicoes(saldolista,0,destinatariosistema)
            trocar_posicoes(historicocompras,0,destinatariosistema)
            trocar_posicoes(historicodepositos,0,destinatariosistema)
            trocar_posicoes(cpf,0,destinatariosistema)

            historico(destinatariosistema,compra,destinatario)

            trocar_posicoes(nome,0,destinatariosistema)
            trocar_posicoes(numeroconta,0,destinatariosistema)
            trocar_posicoes(saldolista,0,destinatariosistema)
            trocar_posicoes(historicocompras,0,destinatariosistema)
            trocar_posicoes(historicodepositos,0,destinatariosistema)
            trocar_posicoes(cpf,0,destinatariosistema)

            saldolista[0] = saldolista[0] - compra

            print('Compra realizada! :D')
            sleep(2)
            pix()
        
        elif saldolista[0] < compra:
            print('Saldo insufuciente para essa compra :(')
            sleep(3)
            pix()

        
    elif escolha == '2':
        #Voltar
        menu()
    
    else:
        print('digite uma opção válida! voltando ao menu TRANFERÊNCIA...')
        sleep(3)
        menu()

def depositar():
    traco()
    print(f"{'DEPÓSITO':^40}")
    print('1-Depositar em sua conta\n',
        '2-Voltar\n')
    traco()
    escolha = input('Escolha um número pra navegar:')

    if escolha == '1':
        traco()
        deposito = float(input('Valor a ser depositado:'))
        saldolista[0] = saldolista[0] + deposito

        historicodep(deposito)

        print('Valor depositado! :D\n')
        sleep(1)
        print('voltando ao menu TRANFERÊNCIA...')
        sleep(2)
        pix()

    elif escolha == '2':
        #Voltar
        menu()
    
    else:
        print('digite uma opção válida! voltanDO ao menu TRANFERÊNCIA...')
        sleep(3)
        pix()

def extrato():
    traco()
    print(f"{'EXTRATO':^40}")
    print('1-Histórico de compras\n',
        '2-Histórico de depositos\n',
        '3-Voltar\n')
    traco()
    escolha = input('Escolha um número pra navegar:')

    if escolha == '1':
        print(f"{'HISTÓRICO(TRANSFERÊNCIAS)':^40}")
        traco()
        
        for y in range(len(historicocompras[0])):
            print('|nome:',historicocompras[0][y][0],'||Preço:R$',historicocompras[0][y][1],'||destinatário:',historicocompras[0][y][2],'||data(horas):',historicocompras[0][y][3], '|\n')
        
        print('\n\n1-Voltar')
        traco()
        escolha = input('Escolha um número pra navegar:')

        if escolha == '1':
            extrato()
        else:
            print('digite uma opção válida! voltando ao menu EXTRATO...')
            sleep(3)
            extrato()

    elif escolha == '2':
        traco()
        print('HISTÓRICO(DEPOSITOS):\n')
        
        for y in range(len(historicodepositos[0])):
            print('|nome:',historicodepositos[0][y][0],'||Preço depositado:R$',historicodepositos[0][y][1],'||data(horas):',historicodepositos[0][y][2],'|\n')
        print('1-Voltar')
        traco()

        escolha = input('Escolha um número pra navegar:')

        if escolha == '1':
            extrato()
        else:
            print('error!!!')
            menu()
    elif escolha == '3':
        #volta
        menu()
    else:
        print('error!!!')
        menu()

menuinicial()