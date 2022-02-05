def menu():
    voltarMenu = 's'
    while voltarMenu == 's':
        opcao = input('''
    *******************************************
                   AGENDA PYTHON
    *******************************************                  
    MENU:
    
    [1] CADASTRAR CONTATOS
    [2] LISTAR CONTATOS
    [3] DELETAR CONTATOS
    [4] BUSCAR CONTATO 
    [5] SAIR
    ********************************************
    ESCOLHA UMA OPÇÃO ACIMA: 
    ''')
        if opcao == '1':
            cadastrarContato()
        elif opcao == '2':
            listarContato()
        elif opcao == '3':
            deletarContato()
        elif opcao == '4':
            buscarContato()
        else:
            sair()
        voltarMenu = input('Deseja voltar ao menu principal? (s/n) ').lower()

def cadastrarContato():
    novoContato = 's'
    while novoContato == 's':
        id = input('Digite o ID do contato: ')
        nome = input('Digite o nome do contato: ')
        telefone = input('Digite o telefone do contato: ')
        email = input('Digite o email do contato: ')

        try:
            agenda = open("agenda.txt", "a")
            dados = f'{id};{nome};{telefone};{email} \n'
            agenda.write(dados)
            agenda.close()
            print(f'Contato gravado com sucesso!!!')
        except:
            print(f'ERRO na gravação do contato!!!')
        novoContato = input('Deseja CADASTRAR um novo contato? (s/n)').lower()

def listarContato():
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        print(contato)
    agenda.close()

def deletarContato():
    deletaNovo = 's'
    while deletaNovo == 's':
        nomeDeletado = input('Digite o nome que deseja deletar: ').lower()
        agenda = open("agenda.txt", "r")
        aux = []
        aux2 = []
        for i in agenda:
            aux.append(i)
        for i in range(0, len(aux)):
            if nomeDeletado not in aux[i].lower():
                aux2.append(aux[i])
        agenda = open("agenda.txt", "w")
        for i in aux2:
            agenda.write(i)
        print(f'Contato deletado com sucesso!')
        listarContato()
        deletaNovo = input('Deseja DELETAR um novo contato? (s/n)').lower()


def buscarContato():
    nome = input(f'Digite o NOME do contato que deseja procurar: ').upper()
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        if nome in contato.split(";")[1].upper():
            print(contato)
    agenda.close()

def sair():
    print(f'Obrigdo pelo acesso! \nAté mais ;)')
    exit()

def main():
    menu()

main()