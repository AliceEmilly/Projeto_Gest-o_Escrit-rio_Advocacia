
def validaNome():
    nome = input("Nome: ")
    while nome == "":
        print()
        print("Nome inválido! Tente novamente!")
        nome = input("Nome: ")
    return nome

def validaEmail():
    email = input("Email: ")
    while (email == "") or ((email.count("@") != 1 or email.count(".") == 0)):
        print()
        print("Email inválido! Tente novamente!")
        email = input("Email: ")
    return email

def validaTelefone():
    fone = input("Telefone: ") 
    foneS = fone.replace("(", "").replace(")", "").replace("-", "")  
    while (fone == "") or (not(foneS.isnumeric()) or (not(len(foneS) == 10 or len(foneS) == 11))):
        print()
        print("Telefone inválido! Tente novamente!")
        fone = input("Telefone: ")
        foneS = fone.replace("(", "").replace(")", "").replace("-", "")
    return fone

def validaCpf_Cnpj():
    cpf_cnpj = input("CPF/CNPJ: ")
    cpf_cnpjS = cpf_cnpj.replace(".", "").replace("-", "").replace("/", "")
    while (cpf_cnpj == "") or (not( cpf_cnpjS.isnumeric()) or (len(cpf_cnpjS) != 11 and len(cpf_cnpjS) != 14)):
        print()
        print("CPF/CNPJ inválido! Tente novamente!")
        cpf_cnpj = input("CPF/CNPJ: ")
        cpf_cnpjS = cpf_cnpj.replace(".", "").replace("-", "").replace("/", "")
    return cpf_cnpj

def validaOab():
    oab = input("Nº da OAB(XXXXXX/YY): ")
    while oab.count("/") != 1:
        print()
        print("OAB inválida! Tente novamente!")
        oab = input("Nº da OAB: ")
    n, uf = oab.split("/")
    while (oab == "") or (not n.isnumeric()) or (len(uf) != 2 or (not(uf.isalpha()))):
        print()
        print("OAB inválida! Tente novamente!")
        oab = input("Nº da OAB: ")
        n, uf = oab.split("/")
    return oab

def validaEspec():
    espec = input("Especialidade: ")
    while espec == "":
        print()
        print("Especialidade inválida! Tente novamente!")
        espec = input("Especialidade: ")
    return espec

def validaNumero():
    num = input("Número do processo(XXXXXXXX-YY): ")
    numS = num.replace("-", "")
    while (num == "") or (not(numS.isnumeric()) or (len(numS) != 9)):
        print()
        print("Número do processo inválido! Tente novamente!")
        num = input("Número do processo: ")
        numS = num.replace("-", "")
    return num

def validaDescricao():
    desc = input("Breve descrição: ")
    while desc == "":
        print("Descrição inválida!Tente novamente!")
        print()
        desc = input("Descrição: ")
    return desc

def validaData():
    data = input("Data do cadastro(XX/YY/XYXY): ")
    while data.count("/") != 2:
        print()
        print("Formato da data inválido! Tente novamente!")
        data = input("Data do cadastro(XX/YY/XYXY): ")
    dia, mes, ano = map(int, data.split('/'))
    while (data == "") or ((ano<=0) or (mes<1 or mes>12) or (dia<=0 or dia>31)):
        print()
        print("Data inválida! Tente novamente!")
        data = input("Data do cadastro(XX/YY/XYXY): ")
        dia, mes, ano = map(int, data.split('/'))
    return data