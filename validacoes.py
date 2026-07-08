from datetime import datetime

def validaNome():
    nome = input("Nome(25 caracteres): ").strip()
    while nome == "":
        print()
        print("O nome não pode ficar em branco. Digite um nome.")
        nome = input("Nome: ").strip()
    return nome

def validaEmail():
    email = input("Email: ").strip()
    while (email == "") or ((email.count("@") != 1) or (email.count(".") == 0)): 
        print()
        print("Email inválido! Use o formato nome@dominio.com, com um único @ e pelo menos um ponto.")
        email = input("Email: ").strip()
    return email

def validaTelefone():
    fone = input("Telefone: ").strip()
    foneS = fone.replace("(", "").replace(")", "").replace("-", "") 
    while (fone == "") or (not(foneS.isnumeric()) or (len(foneS)!= 10 and len(foneS)!= 11)): 
        print()
        print("Telefone inválido! Use o formato (XX)XXXX-XXXX ou (XX)XXXXX-XXXX, só com números.")
        fone = input("Telefone: ").strip()
        foneS = fone.replace("(", "").replace(")", "").replace("-", "")
    return fone

def validaCpf_Cnpj():
    cpf_cnpj = input("CPF/CNPJ do cliente: ").strip()
    cpf_cnpjS = cpf_cnpj.replace(".", "").replace("-", "").replace("/", "")
    while (cpf_cnpj == "") or (not(cpf_cnpjS.isnumeric()) or (len(cpf_cnpjS)!= 11 and len(cpf_cnpjS)!= 14)):
        print()
        print("CPF/CNPJ inválido! Use CPF com 11 dígitos (XXX.XXX.XXX-XX) ou CNPJ com 14 dígitos (XX.XXX.XXX/XXXX-XX).")
        cpf_cnpj = input("CPF/CNPJ: ").strip()
        cpf_cnpjS = cpf_cnpj.replace(".", "").replace("-", "").replace("/", "")
    return cpf_cnpj

def validaOab():
    while True:
        oab = input("Nº da OAB(XXXXXX/UF) do advogado: ").strip()
        if oab.count("/") != 1:
            print()
            print("Formato inválido! A OAB precisa ter uma única barra separando o número da UF, ex: 123456/RN.")
            continue 
        n, uf = oab.split("/")
        if (not n.isnumeric()) or (len(uf)!= 2 or (not(uf.isalpha()))): 
            print()
            print("OAB inválida! O número deve conter só dígitos e a UF deve ter 2 letras, ex: 123456/RN.")
            continue
        return oab 

def validaEspec():
    espec = input("Especialidade(30 cararcteres): ").strip()
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
    desc = input("Breve descrição(40 caracteres): ").strip()
    while desc == "":
        print()
        print("A descrição não pode ficar em branco. Informe um breve resumo do processo.")
        desc = input("Descrição: ").strip()
    return desc

def validaData():
    while True:
        data = input("Data de abertura do processo(DD/MM/AAAA): ").strip()
        if data.count("/") != 2:
            print()
            print("Formato inválido! Use DD/MM/AAAA, com duas barras e apenas números, ex: 05/03/2026.")
            continue
        dia, mes, ano = data.split('/')
        if (not data.replace("/", "").isnumeric()) or (len(dia) != 2 or len(mes) != 2 or len(ano) != 4) or (not (1 <= int(mes) <= 12)) or (not (1 <= int(dia) <= 31)) or (int(ano) <= 0):
            print()
            print("Data inválida! O dia deve ser de 1 a 31, o mês de 1 a 12, e o ano maior que 0.")
            continue
        try:
            datetime.strptime(data, "%d/%m/%Y")
        except ValueError:
            print()
            print("Data inválida! Esse dia não existe nesse mês (ex: 31/02).")
            continue
        return data

def validaMes(mensagem):
    mes = input(mensagem).strip()
    while (not mes.isnumeric()) or (len(mes) != 2) or (not (1 <= int(mes)<= 12)): 
        print()
        print("Mês inválido! Informe um número de 01 a 12, com 2 dígitos.")
        mes = input(mensagem).strip()
    mes = int(mes)
    return mes

def validaAno(mensagem):
    ano = input(mensagem).strip()
    while (not ano.isnumeric()) or (len(ano) != 4) or (int(ano) <= 0):
        print()
        print("Ano inválido! Informe o ano com 4 dígitos (ex: 2026).")
        ano = input(mensagem).strip()
    ano = int(ano)
    return ano

def atualizacaoNome(nome, validaNome):
    pergunta = input("Deseja manter o nome atual(S/N)? ").strip()
    valorAtual = nome
    if pergunta.strip().lower() == "s":
        return valorAtual
    else:
        print()
        return validaNome()

def atualizacaoTelefone(telefone, validaTelefone):
    pergunta = input("Deseja manter o telefone atual(S/N)? ").strip()
    valorAtual = telefone
    if pergunta.strip().lower() == "s":
        return valorAtual
    else:
        print()
        return validaTelefone()

def atualizacaoEmail(email, validaEmail):
    pergunta = input("Deseja manter o email atual(S/N)? ").strip()
    valorAtual = email
    if pergunta.strip().lower() == "s":
        return valorAtual
    else:
        print()
        return validaEmail()