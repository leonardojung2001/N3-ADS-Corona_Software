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
    return nome


def arquivo_existe(nome):
    global arq
    arq = nome
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def cabecalho():
    print('*' * 40)
    print('*', ' ' * 36, '*')
    print(f'{"* Professor: Roberto Fabiano": <38} *')
    print(f'{"* Aluno: Lucas Aguiar": <38} *')
    print(f'{"* Curso: ADS": <38} *')
    print(f'{"* Estudante da Faculdade Cesusc": <38} *')
    print('*', ' ' * 36, '*')
    print('*' * 40)


def opcoes():
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


def lista_de_paciente():
    print(f'{"Pacientes Cadastrados:":-^40}')
    print('-' * 40)
    try:
        arquivo = open(arq, "r")
        for linha in arquivo:
            linha_lista = linha.split(',')
            print(linha_lista[0])
        arquivo.close()
    except IOError as error:
        print(f'ERRO: {error}')


def opcoes_de_alterar_dados_do_pacientes():
    global opcao_de_alteracao
    print('-' * 40)
    print(f'{"Dados Para Alteração":-^40}')
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
    opcao_de_alteracao = int(input('Qual Dado Deseja Alterar: '))
    return opcao_de_alteracao


def alterar_dados_do_pacientes():
    print('-' * 40)
    try:
        with open(arq, 'r') as arquivo:
            nome_alteracao = str(input('Digite o Nome do Paciente que Desenha Alterar o Dado: ')).title()
            linhas = arquivo.readlines()
            for elemento in linhas:
                if elemento.startswith(nome_alteracao):
                    print('- ' * 20)
                    print(f'Alterando dado de {nome_alteracao}.')
                    print('- ' * 20)
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
                    pos = linhas.index(elemento)
                    item = (nome + ',' + cns + ',' + bairro + ',' + unidade_de_saude + ',' + data_nascimento +
                            ',' + comobirdaes + ',' + data_de_inicio_dos_sintomas + ',' + endereco +
                            ',' + sintomas_iniciais + ',' + telefone1 + ',' + telefone2 + '\n')
                    linhas.pop(pos)
                    linhas.insert(pos, item)
                    arquivo = open(arq, 'w')
                    arquivo.writelines(linhas)
                    arquivo.close()
                    print('- ' * 20)
                    print('Mudança feita com sucesso!!')
                    return
        print('- ' * 20)
        print(f'Nome de {nome_alteracao} Não Encontrado')
    except:
       print(f'Error')


# def excluir_dados_do_pacientes():
#
#
# def realizar_backup_do_arquivo


# Verificação/Criação do arquivo
arq = 'Dados.txt'
if not f.arquivo_existe(arq):  # Caso não existe um arquivo com o nome passado ele irá criar um.
    f.criar_arquivo(arq)  # Caso já tenha um arquivo com o nome passado ele irá ignorar.

# Programa Principal
while True:
    opcao = f.opcoes()
    if opcao == 1:
        f.cadastrar_paciente()
    if opcao == 2:
        f.lista_de_paciente()
    if opcao == 3:
#         f.opcoes_de_alterar_dados_do_pacientes()   No momento nao vamos utilizar
        f.alterar_dados_do_pacientes()
    if opcao == 4:
        print('Opcao chegará em breve')
    if opcao == 5:
        print('Opcao chegará em breve')
    if opcao == 0:
        print('Volte Sempre!!')
        break
