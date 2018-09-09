def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print("Valor inválido, digite um valor válido.\n")


def menu():
    print("""
    1 - Criar arquivo
    2 - Abrir o arquivo
    3 - Apagar e Reescrever o arquivo
    4 - Escrever um novo registro
    5 - Alterar Registro
    6 - Ler posição
    7 - Lê o arquivo
    8 - Fechar o arquivo
    
    0 - Sai
    """)

    return valida_faixa_inteiro("- Escolha uma opção -\n", 0, 7)


def criar():
    arquivo = open("lista_pessoas.txt", "x")
    arquivo.close()
    print("Arquivo criado com sucesso. O nome do seu arquivo é lista_pessoas.txt\n")


def abrir():
    arquivo = open("lista_pessoas.txt", "r")
    print("--------------")
    print(arquivo.read(), "\n--------------\n")


def reescrever():
    arquivo = open("lista_pessoas.txt", "x")
    arquivo.close()
    print("Arquivo lista_pessoas.txt foi apagado e reescrito com sucesso.\n")

def checar_regristro(lista, id):
    for registro in lista:
        if(registro[0] == id):
            return False
    return True


def adicionar():
    lista_pesssoas = []
    arquivo = open("lista_pessoas.txt", "r")
    for linha in arquivo.readlines():
        id, nome, telefone, valor = linha.strip().split("#")
        lista_pesssoas.append([id, nome, telefone, valor])
    print(lista_pesssoas)
    arquivo.close()
    id  = input("Digite o seu ID: ")
    nome = input("Digite o seu nome: ")
    telefone = input("Digite o seu telefone: ")
    valor = input("Digite o valor pago: ")
    if(checar_regristro(lista_pesssoas, id)):
            arquivo = open("lista_pessoas.txt", "a")
            arquivo.write("%s#%s#%s#%s\n" % (id, nome, telefone, valor))
    else:
        print("O registro já existe.")
    arquivo.close()


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
        if opcao == 5:
            adicionar()