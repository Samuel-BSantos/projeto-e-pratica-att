escolha = 0
saldo = 0
nome = []
cpf = []
numeroconta = []
saldolista = []
historicocompras = []
historicodepositos = []
datalista = []
horalista = []
nomeordem = []

def traco(x = 50):
    for i in range(0, x):
        print("=", end='')
    print("\n")

def trocar_posicoes(lista, pos1, pos2):
    lista[pos1], lista[pos2] = lista[pos2], lista[pos1]
    return lista

def menu():
    traco()
    print('Bem vindo!\n')
    print('Digite o número indicado para navegar:\n')
    print('1-Cadastrar\n',
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
        
def cadastro():
    traco()
    print('CADASTRO:\n',
            '1-Criar conta\n',
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
        '3-Alterar conta\n',
        '4-Voltar\n')
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
        alterarconta = input('Digite o cpf da conta que você deseja usar')

        posicaolista = cpf.index(alterarconta)
        trocar_posicoes(nome,0,posicaolista)
        trocar_posicoes(numeroconta,0,posicaolista)
        trocar_posicoes(saldolista,0,posicaolista)
        trocar_posicoes(cpf,0,posicaolista)

        print('Conta alterada com sucesso!')
        traco()

        menu()

    elif escolha == 4:
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
            data = input('Digite o dia més e ano da compra(ex: xx/xx/xxxx):')
            hora = input('Digite a hora da compra(ex: xx:xx):')

            saldolista[0] = saldolista[0] - compra

            historicocompras.append(compra)
            horalista.append(hora)
            datalista.append(data)
            nomeordem.append(nome)

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

        historicodepositos.append(deposito)

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

        for x in historicocompras:
            print(nomeordem[historicocompras.index(x)], 'R$', x, datalista[historicocompras.index(x)], horalista[historicocompras.index(x)], '\n')
            print('1-Voltar')

            escolha = int(input('Escolha um número pra navegar:'))

            if escolha == 1:
                extrato()
            else:
                print('error!!!')
                menu()

    elif escolha == 2:
        traco()
        print('HISTÓRICO(DEPOSITOS):\n')
        
        for x in historicodepositos:
            print('-- R$', x)
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

menu()