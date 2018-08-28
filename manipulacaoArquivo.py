agenda = []


def pede_nome():
    return input('Nome: ')


def pede_rg():
    return input('Por favor digite o seu RG: ')


def pede_telefone():
    return input('Por favor digite o seu telefone: ')


def pagou():
    return True;


def mostrar_dados(nome, rg, telefone, pagou):
    print('Nome: %s. RG: %s. Telefone: %s - Pagou a entrada: ' % nome, rg, telefone, pagou and 'Sim' or 'Não')

def pede_nome_arquivo():
    return input('Qual o nome do arquivo que deseja: ')





