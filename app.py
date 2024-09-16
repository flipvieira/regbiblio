is_on = True
#This comment is a test for git.

class Cliente:
    def __init__(self, nome, data_nasc, data_reg, cpf, iden):
        self.nome = nome
        self.data_nasc = data_nasc
        self.data_reg = data_reg
        self.cpf = cpf
        self.iden = iden


class Livro:
    def __init__(self, titulo, editora, data_pub, data_reg, sob_autor, iden):
        self.titulo = titulo
        self.editora = editora
        self.data_pub = data_pub
        self.data_reg = data_reg
        self.sob_autor = sob_autor
        self.iden = iden


class Emprestimo:
    def __init__(self, idencliente, idenlivro, data_ini, idenemp):
        self.idencliente = idencliente
        self.idenlivro = idenlivro
        self.data_ini = data_ini
        self.idenemp = idenemp

class Devolucao:
    def __init__(self, idenemp, data_dev):
        self.idenemp = idenemp
        self.data_dev = data_dev


def reg_cliente():
    print("\nREGISTRO DE CLIENTES\nPor favor, insira as informações a seguir.")
    nome = input("Nome completo: ")
    data_nasc = input("Data de nascimento: ")
    data_reg = input("Data do registro: ")
    cpf = input("CPF: ")
    novo_cliente = Cliente(nome, data_nasc, data_reg, cpf, iden=nome[0:2].upper() + data_nasc[6:] + data_reg + cpf[9:])
    dados_novo_cliente = f'{novo_cliente.nome}, {novo_cliente.data_nasc}, {novo_cliente.data_reg}, {novo_cliente.cpf}, {novo_cliente.iden}'

    with open('BD_clientes.txt') as bdclientes:
        bdc_lines = bdclientes.readlines()
        if f'{dados_novo_cliente}\n' in bdc_lines:
                print('Usuário já cadastrado.\n')
                call_menu()
        elif f'{dados_novo_cliente}\n' not in bdc_lines:
            with open('BD_clientes.txt', 'a') as bdclientes_w:
                bdclientes_w.write(f'{dados_novo_cliente}\n')
                print("Usuário registrado com sucesso!\n")

def reg_livro():
    print("\nREGISTRO DE LIVROS\nPor favor, insira as informações a seguir.")
    titulo = input("Título (Formato: Substantivo, Artigo): ")
    editora = input("Editora: ")
    data_pub = input("Ano de publicação: ")
    data_reg = input("Data do registro: ")
    sob_autor = input("Sobrenome do autor: ")
    novo_livro = Livro(titulo, editora, data_pub, data_reg, sob_autor, iden=sob_autor[0:2].upper() + editora[0:2].upper() + titulo[0:2].upper() + data_pub[2:] + data_reg[2:])
    dados_novo_livro = f'{novo_livro.titulo}, {novo_livro.editora}, {novo_livro.data_pub}, {novo_livro.data_reg}, {novo_livro.sob_autor}, {novo_livro.iden}'

    with open('BD_livros.txt') as bdlivros:
        bdl_lines = bdlivros.readlines()
        if f'{dados_novo_livro}\n' in line:
                print("Livro já cadastrado.\n")
                call_menu()
        elif f'{dados_novo_livro}\n' not in bdl_lines:
            with open('BD_livros.txt', 'a') as bdlivros_w:
                bdlivros_w.write(f'{dados_novo_livro}\n')
                print("Livro registrado com sucesso!\n")

def reg_emprestimo():
    print("\nREGISTRO DE EMPRÉSTIMO\nPor favor, insira as informações a seguir.")
    idencliente = input("ID do cliente: ")
    idenlivro = input("ID do livro: ")
    data_ini = input("Data do empréstimo: ")
    novo_emprestimo = Emprestimo(idencliente, idenlivro, data_ini, idenemp=idenlivro + idencliente)
    dados_novo_emprestimo = f'{novo_emprestimo.idencliente}, {novo_emprestimo.idenlivro}, {novo_emprestimo.data_ini}, {novo_emprestimo.idenemp}'

    with open('BD_processos.txt') as bdprocessos:
        bdp_lines = bdprocessos.readlines()
        if f'{dados_novo_emprestimo}\n' in line:
                print("Empréstimo já cadastrado.\n")
                call_menu()
        elif f'{dados_novo_emprestimo}\n' not in bdp_lines:
            with open('BD_processos.txt', 'a') as bdprocessos_w:
                bdprocessos_w.write(f'{dados_novo_emprestimo}\n')
                print('Empréstimo registrado com sucesso!\n')

def reg_devol():
    print("REGISTRO DE DEVOLUÇÕES\nPor favor, insira as informações a seguir.")
    idenemp = input("Código do empréstimo: ")
    data_dev = input("Data da devolução: ")
    nova_devolucao = Devolucao(idenemp, data_dev)
    dados_nova_devolucao = f'{nova_devolucao.idenemp}, {nova_devolucao.data_dev}'

    with open('BD_devolucoes.txt') as bddevolucoes:
        bdd_lines = bddevolucoes.readlines()
        if f'{dados_nova_devolucao}\n' in line:
                print('Devolução já registrada.\n')
                call_menu()
        elif f'{dados_nova_devolucao}\n' not in bdd_lines:
            with open('BD_devolucoes.txt', 'a') as bddevolucoes_w:
                bddevolucoes_w.write(f'{dados_nova_devolucao}\n')
                print('Devolução registrada com sucesso!\n')

def call_menu():
    print('BEM VINDO AO REGBIBLIO 1.0!\nPara continuar, digite um comando e pressione enter.\nSe precisa de ajuda para receber uma lista de comandos, digite "ajuda" e pressione enter.\nPara fechar o RegBiblio 1.0, digite "sair" e pressione enter.')
    global is_on
    comandos_validos = ('regcliente', 'reglivro', 'regemp', 'regdevol', 'ajuda', 'sair')
    comando = input("Inserir comando: ")
    if comando not in comandos_validos:
        print('Comando inválido.')
        call_menu()
    elif comando == 'regcliente':
        reg_cliente()
    elif comando == 'reglivro':
        reg_livro()
    elif comando == 'regemp':
        reg_emprestimo()
    elif comando == 'regdevol':
        reg_devol()
    elif comando == 'ajuda':
        ajuda()
    elif comando == 'sair':
        is_on = False

def ajuda():
    print('LISTA DE COMANDOS REGBIBLIO 1.0:\n\n- "regcliente": iniciar registro de clientes;\n- "reglivro": iniciar registro de livros;\n- "regemp": iniciar registro de empréstimos;\n- "regdevol": iniciar registro de devoluções;\n-"ajuda": exibe esta lista de comandos;\n')
    call_menu()

while is_on:
    call_menu()
    if not is_on:
        break
