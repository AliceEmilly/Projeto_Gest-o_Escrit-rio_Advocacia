def validaNome():
    nome = input("Nome: ").strip()
    while nome == "":
        print()
        print("O nome não pode ficar em branco. Digite o nome completo.")
        nome = input("Nome: ").strip()
    return nome

def validaEmail():
    email = input("Email: ").strip()
    while (email == "") or ((email.count("@") != 1 or email.count(".") == 0)):
        print()
        print("Email inválido! Use o formato nome@dominio.com, com um único @ e pelo menos um ponto.")
        email = input("Email: ").strip()
    return email

def validaTelefone():
    fone = input("Telefone: ").strip()
    foneS = fone.replace("(", "").replace(")", "").replace("-", "")  
    while (fone == "") or (not(foneS.isnumeric()) or (not(len(foneS) == 10 or len(foneS) == 11))):
        print()
        print("Telefone inválido! Use o formato (XX)XXXX-XXXX ou (XX)XXXXX-XXXX, só com números.")
        fone = input("Telefone: ").strip()
        foneS = fone.replace("(", "").replace(")", "").replace("-", "")
    return fone

def validaCpf_Cnpj():
    cpf_cnpj = input("CPF/CNPJ do cliente: ").strip()
    cpf_cnpjS = cpf_cnpj.replace(".", "").replace("-", "").replace("/", "")
    while (cpf_cnpj == "") or (not( cpf_cnpjS.isnumeric()) or (len(cpf_cnpjS) != 11 and len(cpf_cnpjS) != 14)):
        print()
        print("CPF/CNPJ inválido! Use CPF com 11 dígitos (XXX.XXX.XXX-XX) ou CNPJ com 14 dígitos (XX.XXX.XXX/XXXX-XX).")
        cpf_cnpj = input("CPF/CNPJ: ").strip()
        cpf_cnpjS = cpf_cnpj.replace(".", "").replace("-", "").replace("/", "")
    return cpf_cnpj

def validaOab():
    oab = input("Nº da OAB(XXXXXX/UF) do advogado: ").strip()
    while oab.count("/") != 1:
        print()
        print("Formato inválido! A OAB precisa ter uma única barra separando o número da UF, ex: 123456/RN.")
        oab = input("Nº da OAB: ")
    n, uf = oab.split("/")
    while (oab == "") or (not n.isnumeric()) or (len(uf) != 2 or (not(uf.isalpha()))):
        print()
        print("OAB inválida! O número deve conter só dígitos e a UF deve ter 2 letras, ex: 123456/RN.")
        oab = input("Nº da OAB: ").strip()
        n, uf = oab.split("/")
    return oab

def validaEspec():
    espec = input("Especialidade: ").strip()
    while espec == "":
        print()
        print("A especialidade não pode ficar em branco. Informe a área de atuação do advogado.")
        espec = input("Especialidade: ").strip()
    return espec

def validaNumero():
    num = input("Número do processo(XXXXXXXX-YY): ").strip()
    numS = num.replace("-", "")
    while (num == "") or (not(numS.isnumeric()) or (len(numS) != 9)):
        print()
        print("Número inválido! Use o formato XXXXXXXX-YY, com 9 dígitos no total, só números e um traço.")
        num = input("Número do processo: ").strip()
        numS = num.replace("-", "")
    return num

def validaDescricao():
    desc = input("Breve descrição: ").strip()
    while desc == "":
        print("A descrição não pode ficar em branco. Informe um breve resumo do processo.")
        print()
        desc = input("Descrição: ").strip()
    return desc

def validaData():
    data = input("Data do cadastro(DD/MM/AAAA: ").strip()
    while data.count("/") != 2:
        print()
        print("Formato inválido! Use DD/MM/AAAA, com duas barras, ex: 05/03/2026.")
        data = input("Data do cadastro(DD/MM/AAAA): ")
    dia, mes, ano = map(int, data.split('/'))
    while (data == "") or ((ano<=0) or (mes<1 or mes>12) or (dia<=0 or dia>31)):
        print()
        print("Data inválida! O dia deve ser de 1 a 31, o mês de 1 a 12, e o ano maior que 0.")
        data = input("Data do cadastro(DD/MM/AAAA): ").strip()
        dia, mes, ano = map(int, data.split('/'))
    return data

def validaMes(mensagem):
    mes = input(mensagem)
    while (len(mes) != 2) or (not mes.isnumeric()) or (not (1 <= int(mes) <= 12)):
        print()
        print("Mês inválido! Informe um número de 01 a 12, com 2 dígitos.")
        mes = input(mensagem)
    mes = int(mes)
    return mes

def validaAno(mensagem):
    ano = input(mensagem)
    while (len(ano) != 4) or (not ano.isnumeric()):
        print()
        print("Ano inválido! Informe o ano com 4 dígitos (ex: 2026).")
        ano = input(mensagem)
    ano = int(ano)
    return ano

def atualizacaoNome(nome, validaNome):
    pergunta = input("Deseja manter o nome atual(S/N)? ")
    valorAtual = nome
    if pergunta.lower() == "s":
        return valorAtual
    else:
        print()
        return validaNome()

def atualizacaoTelefone(telefone, validaTelefone):
    pergunta = input("Deseja manter o telefone atual(S/N)? ")
    valorAtual = telefone
    if pergunta.lower() == "s":
        return valorAtual
    else:
        print()
        return validaTelefone()

def atualizacaoEmail(email, validaEmail):
    pergunta = input("Deseja manter o email atual(S/N)? ")
    valorAtual = email
    if pergunta.lower() == "s":
        return valorAtual
    else:
        print()
        return validaEmail()