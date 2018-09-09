lista_pessoas = []


def pede_nome():
    return input('Nome: ')


def pede_rg():
    return input('Por favor digite o seu RG: ')


def pede_telefone():
    return input('Por favor digite o seu telefone: ')


def pede_pagou():
    return input('Por favor digite s - para pagou ou n - para não pagou').lower()


def mostrar_dados(nome, rg, telefone, pagou):
    print('Nome: %s. RG: %s. Telefone: %s - Pagou a entrada: ' % nome, rg, telefone, pagou and 'Sim' or 'Não')


def pede_nome_arquivo():
    return input('Qual o nome do arquivo que deseja: ')


def pesquisa_nome(nome):
    mnome = nome.lower()
    for p, e in enumerate(lista_pessoas):
        if e[0].lower() == mnome:
            return p
    return None


def pesquisa_rg(rg):
    for p, e in enumerate(lista_pessoas):
        if e[1] == rg:
            return p
    return None


def novo_registro():
    global lista_pessoas
    rg = pede_rg()
    p = pesquisa_rg(rg)
    if p is not None:
        print('O Registro já existe.')
        return
    nome = pede_nome()
    telefone = pede_telefone()
    pagou = False;
    if pede_pagou() == 's':
        pagou = True
    else:
        lista_pessoas.append([nome, rg, telefone, pagou])
        print('O registro foi salvo no arquivo.')


def apaga_registro():
    p = pesquisa_rg(pesquisa_rg())
    if p is not None:
        del lista_pessoas[p]
    else:
        print('Registro não encontrado.')


def altera_registro():
    p = pesquisa_rg(pede_rg())
    if p is not None:
        nome = lista_pessoas[p][0]
        rg = lista_pessoas[p][1]
        telefone = lista_pessoas[p][2]
        pagou = lista_pessoas[p][3]
        print('Encontrado.')
        mostrar_dados(nome, rg, telefone, pagou)
        nome = pede_nome()
        rg = pede_rg()
        telefone = pede_telefone()
        pagou = pede_pagou()
        lista_pessoas[p] = [nome, rg, telefone, pagou]
    else:
        print('Não encontrado')


def lista():
    print('---- Lista de pessoas que participarão do evento --------')
    for e in lista_pessoas:
        mostrar_dados(e[0], e[1], e[2], e[3])
        print('-------\n')
