def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print('Valor inválido, digite um valor válido.\n')


def menu():
    print("""
    1 - Criar arquivo
    2 - Abrir e ler arquivo
    3 - Apagar e Reescrever o arquivo
    4 - Escrever um novo registro
    5 - Alterar Registro
    6 - Ler posição
    7 - Adicionar registro em uma posição específica
    8 - Deletar arquivo
    
    0 - Sai
    """)

    return valida_faixa_inteiro('- Escolha uma opção -\n', 0, 7)


def criar():
    arquivo = open('lista_pessoas.txt', 'x')
    arquivo.close()
    print('Arquivo criado com sucesso. O nome do seu arquivo é lista_pessoas.txt\n')


def abrir():
    arquivo = open('lista_pessoas.txt', 'r')
    for linha in arquivo.readlines():
        id, nome, telefone, valor = linha.strip().split("#")
        if id != "":
            print('Id: %s\nNome: %s\nTelefone: %s\nValor: R$ %s' % (id, nome, telefone, valor))
            print('--------------')



def reescrever():
    arquivo = open('lista_pessoas.txt', 'x')
    arquivo.close()
    print('Arquivo lista_pessoas.txt foi apagado e reescrito com sucesso.\n')


def checar_regristro(lista, id):
    for registro in lista:
        if (registro[0] == id):
            return False
    return True


def get_input():
    nome = input('Digite o nome: ')
    telefone = input('Digite o telefone: ')
    valor = input('Digite valor pago: ')
    return nome, telefone, valor


def append_lista(id, nome, telefone, valor):
    arquivo = open('lista_pessoas.txt', 'a')
    arquivo.write("%s#%s#%s#%s\n" % (id, nome, telefone, valor))
    arquivo.close()


def criar_lista():
    lista_pesssoas = []
    arquivo = open('lista_pessoas.txt', 'r')
    for linha in arquivo.readlines():
        id, nome, telefone, valor = linha.strip().split("#")
        lista_pesssoas.append([id, nome, telefone, valor])
    arquivo.close()
    return lista_pesssoas


def adicionar():
    lista_pesssoas = criar_lista()
    id = input('Digite o ID: ')
    nome, telefone, valor = get_input()
    if (checar_regristro(lista_pesssoas, id)):
        append_lista(id, nome, telefone, valor)
    else:
        print('O registro já existe.\n')


def alterar():
    lista_pessoas = criar_lista()
    id = input('Digite o id que deseja alterar: ')
    for pessoa in lista_pessoas:
        if pessoa[0] == id:
            nome, telefone, valor = get_input()
            append_lista(id, nome, telefone, valor)
        else:
            print('Não existe registro com esse id.\n')


def ler_posicao():
    arquivo = open('lista_pessoas.txt')
    lines = arquivo.readlines()
    posicao = int(input('Digite a posicao que deseja imprimir: '))
    if lines[posicao] is not None:
        id, nome, telefone, valor = lines[posicao].strip().split("#")
        print('Id: %s\nNome: %s\nTelefone: %s\nValor: R$ %s' % (id, nome, telefone, valor))
    else:
        print('A posicao não existe')



def posicao_especifica():
    posicao = int(input('Digite a posicao que deseja adicionar '))
    lista_pessoas = criar_lista()
    id = input('Digite o ID: ')
    nome, telefone, valor = get_input()
    if (checar_regristro(lista_pessoas, id)):
        if(len(lista_pessoas) < posicao):
            for i in range(len(lista_pessoas), posicao+1):
                lista_pessoas.append(["","","","",""])
            lista_pessoas[posicao] = [id, nome, telefone, valor]
            arquivo = open('lista_pessoas.txt', 'w')
            for pessoa in lista_pessoas:
                arquivo.write("%s#%s#%s#%s\n" % (pessoa[0], pessoa[1], pessoa[3], pessoa[3]))
            arquivo.close()
        else:
            if lista_pessoas[posicao][0] != "":
                print('Registro nesta posicao já existe.')
            else:
                lista_pessoas[posicao] = [id, nome, telefone, valor]
                arquivo = open('lista_pessoas.txt', 'w')
                for pessoa in lista_pessoas:
                    arquivo.write("%s#%s#%s#%s\n" % (pessoa[0], pessoa[1], pessoa[3], pessoa[3]))
                arquivo.close()
    else:
        print('Registro com esse id já existe.')


if __name__ == "__main__":
    while True:
        opcao = menu()
        if opcao == 0:
            break
        if opcao == 1:
            criar()
        if opcao == 2:
            abrir()
        if opcao == 3:
            reescrever()
        if opcao == 4:
            adicionar()
        if opcao == 5:
            alterar()
        if opcao == 6:
            ler_posicao()
        if opcao == 7:
            posicao_especifica()
