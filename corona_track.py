global j

def criarArquivo(nome):
    global arq  # Variavel qur estáva no escopo local passa a ser global para acessar em outros lugares.
    arq = nome
    try:
        arquivo = open(nome, 'wt+')  # Cria um aquivo em formato de escrita e leitura
        arquivo.close()  # Fecha o arquivo
    except:
        print(
            'Houve um erro na criação do arquivo!')  # Caso de algum erro na hora de criar o arquivo uma msg irá aparecer.
    else:
        print(
            f'Aquivo {nome} criado com sucesso!')  # Caso nao tenha erro na hora de criar o arquivo uma msg irá aparecer.


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def cabecalho():
    print('*' * 40)
    print('*', ' ' * 36, '*')
    print(f'{"* Professor: Roberto Fabiano": <38} *')
    print(f'{"* Aluno: Lucas Aguiar e Leonardo Jung": <38} *')
    print(f'{"* Curso: ADS": <38} *')
    print(f'{"* Estudante da Faculdade Cesusc": <38} *')
    print('*', ' ' * 36, '*')
    print('*' * 40)


def opcoes():
    global opcao
    print(f'{"Escola a Opção:":-^40}')
    print('-' * 40)
    print('1 - Cadastrar Paciente')
    print('2 - Listar Pacientes')
    print('3 - Alterar Dados do Pacientes')
    print('4 – Excluir Dados do Pacientes')
    print('5 – Realizar Backup do arquivo')
    print('')
    print('0 - Sair')
    print('-' * 40)
    opcao = int(input('Digite Sua Opção: '))
    print('')
    return opcao


def cadastrar_paciente():
    try:
        arquivo = open(arq, 'a')

        print(f'{"Cadastro de Novo Paciente":-^40}')
        print('-' * 40)

        nome = str(input('Nome do Paciente: ')).title()
        cns = input('CNS: ')
        bairro = input('Bairro: ')
        unidade_de_saude = input('Unidade de Saúde: ')
        data_nascimento = input('Data de nascimento: ')
        comobirdaes = input('Comorbidades: ')
        data_de_inicio_dos_sintomas = input('Data de Início dos Sintomas: ')
        endereco = input('Endereço: ')
        sintomas_iniciais = input('Sintomas Inícias: ')
        telefone1 = input('Telefone1: ')
        telefone2 = input('Telefone2: ')
        
        if telefone1 or telefone2 == '':
            print('É necessario um Telefone de contato para concluir o cadastro!!')
            telefone2 = input('Telefone1: ')
        # registrar os dados
        arquivo.write(nome + ',' + cns + ',' + bairro + ',' + unidade_de_saude + ',' + data_nascimento +
                      ',' + comobirdaes + ',' + data_de_inicio_dos_sintomas + ',' + endereco +
                    ',' + sintomas_iniciais + ',' + telefone1 + ',' + telefone2 + '\n')
   



        arquivo.close()
        print('')
        print(f'Cadastro de {nome} concluído')

    except IOError as error:
        print(f'ERRO: {error}')


def lista_de_paciente():      #mudei aqui s2
    print(f'{"Pacientes Cadastrados:":-^40}')
    print('-' * 40)

    try:
        arquivo = open(arq, "r")
        lista_de_dados = arquivo.readlines() #interpreta todos os dados cadastrador (para cada usuario) como lista  
       # print(lista_de_dados[0])

        nova_lista = []
        
        for dado in lista_de_dados: #esse "for" aqui cria uma matriz, para acessar os dados como se fosse uma lista e nao string
            nova_lista.append(dado.split(","))

        #essa variavel serve para manter o controle
        contador = 0

        while(contador < len(nova_lista)):
            print(nova_lista[contador][0])  #ou seja imprima sempre o primeiro index das listas dentro da lista
            contador += 1

        arquivo.close()

    except IOError as error:
        print(f'ERRO: {error}')


def alterar_dados_do_pacientes():  #mudei tbm s2
    print('-' * 40)
    try:
        arquivo = open(arq, 'r+')
    except:
        print('Error')
    else:
        nome_alteracao = str(input('Nome do Paciente: ')).title()
        print('')

        elemento = []

        

        for ele in arquivo.readlines():
            ele = ele.strip()
            elemento.append(ele.split(","))



        if nome_alteracao in [j for i in elemento for j in i]:   #checando existencia do nome digitado na lista de lista usando iteracao
            # a partir do nome vamos pegar sua lista correspondente
            for l in range(len(elemento)):
                for c in range(len(elemento[0])):
                    if elemento[l][c] == nome_alteracao:
                        lista_corresp = elemento[l]
                        print(elemento)
                        break

            print('-' * 40)
            print('0  - Nome do Paciente\n'
                      '1  - CNS\n'
                      '2  - Bairro\n'
                      '3  - Unidade de Saúde\n'
                      '4  - Data de nascimento\n'
                      '5  - Comorbidades\n'
                      '6  - Data de Início dos Sintomas\n'
                      '7  - Endereço\n'
                      '8  - Sintomas Inícias\n'
                      '9  - Telefone1\n'
                      '10 - Telefone2')
            print('-' * 40)

            valor = int(input('Qual Dado Deseja Alterar: '))

            if valor == 0:
                nome = str(input('Nome do Paciente: ')).title()
                #arquivo.write(lista_corresp.replace(lista_corresp[0], nome))
                lista_corresp[0] = nome
                arquivo.writelines(lista_corresp)
            elif valor == 1:
                cns = input('CNS: ')
            elif valor == 2:
                bairro = input('Bairro: ')
            elif valor == 3:
                unidade_de_saude = input('Unidade de Saúde: ')
            elif valor == 4:
                data_nascimento = input('Data de nascimento: ')
            elif valor == 5:
                comobirdades = input('Comorbidades: ')
            elif valor == 6:
                data_de_inicio_dos_sintomas = input('Data de Início dos Sintomas: ')
            elif valor == 7:
                endereco = input('Endereço: ')
            elif valor == 8:
                sintomas_iniciais = input('Sintomas Inícias: ')
            elif valor == 9:
                telefone1 = input('Telefone1: ')
            elif valor == 10:
                telefone2 = input('Telefone2: ')
            print('')
            print('Mudança feita com sucesso!!')

        else:
            print(f'Nome de {nome_alteracao} não encontrado!')
            exit()

    arquivo.close()


# def excluir_dados_do_pacientes():
#
#
# def realizar_backup_do_arquivo():


# Verificação/Criação do arquivo
arq = 'Lucas.txt'
if not arquivo_existe(arq):  # Caso não existe um arquivo com o nome passado ele irá criar um.
    criarArquivo(arq)  # Caso já tenha um arquivo com o nome passado ele irá ignorar.

# Programa Principal
while True:
    opcoes()
    if opcao == 1:
        cadastrar_paciente()
    if opcao == 2:
        lista_de_paciente()
    if opcao == 3:
        alterar_dados_do_pacientes()
    if opcao == 0:
        print('Volte Sempre!!')
        break

