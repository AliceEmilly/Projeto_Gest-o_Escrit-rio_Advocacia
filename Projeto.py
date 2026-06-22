import os
import pickle

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

clientes= {}
try:
    arq_clientes = open("clientes.dat", "rb")
    clientes = pickle.load(arq_clientes)
    arq_clientes.close()
except:
    clientes = {
        "333.333.333-33": ["Fred Flinstone", "(66)66666-6666", "fred@flinstone.com", "Ativo"],
        "22.222.222/2222-22": ["Empresa X", "(77)77777-7777", "x@empresa.com", "Inativo"]
    }
    arq_clientes = open("clientes.dat", "wb")
    pickle.dump(clientes, arq_clientes)
    arq_clientes.close

advogados= {}
try:
    arq_advogados = open("advogados.dat", "rb")
    advogados = pickle.load(arq_advogados) 
    arq_advogados.close()
except:
    advogados = {
        "78901/PB": ["Jack McCoy", "Direito Penal", "(55)55555-5555", "jack@gmail.com", "Ativo"],
        "45232/CE": ["Matt Murdock","Direito Civil e Trabalhista", "(70)70707-0707", "matt@gmail.com", "Ativo"]    
    }
    arq_advogados = open("advogados.dat", "wb")
    pickle.dump(advogados, arq_advogados)
    arq_advogados.close

processos= {}
try:
    arq_processos = open("processos.dat", "rb")
    processos = pickle.load(arq_processos)
    arq_processos.close()
except:
    processos = {
        "0005621-07": ["Ação Penal por Homicídio", "Fred Flinstone", "Jack McCoy", "21/05/2026", "Ativo"],
        "0002847-33": ["Reclamação Trabalhista Rescisória", "Empresa X",  "Matt Murdock", "10/02/2026", "Encerrado"]
    }
    arq_processos = open("processos.dat", "wb")
    pickle.dump(processos, arq_processos)
    arq_processos.close

func = True
while func:
  print()
  print("--------------------------------------------------")
  print("|\tPROJETO AES-ESCRITÓRIO DE ADVOCACIA\t |")
  print("--------------------------------------------------")
  print()
  print("1) Módulo Clientes")
  print("2) Módulo Advogados")
  print("3) Módulo Processos")
  print("4) Módulo Relatórios")
  print("5) Módulo Informações ")
  print("0) Sair do Programa ")
  print()
  op = input("Escolha um número/opção: ")
  os.system('cls' if os.name == 'nt' else 'clear')
  print()
  
  if op == "1":
    while True:
        print("\t\t---MÓDULO CLIENTES---")
        print()
        print("1- Cadastrar Cliente")
        print("2- Visualizar Dados do Cliente")
        print("3- Atualizar Dados do Cliente")
        print("4- Desativar Cliente")
        print("0- Retornar ao Menu Principal")
        print()
        acao = input("Escolha a ação que você deseja realizar: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        
        if acao == "1":
            print("\t\t   ---CADASTRAR CLIENTE---")
            nome = validaNome()
            cpf_cnpj = validaCpf_Cnpj()
            if cpf_cnpj in clientes:
                print("Esse cliente já foi cadastrado!!")
                print("\t\t--------------------")
                input("Tecle ENTER para voltar ao menu de clientes...")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                email = validaEmail()
                telefone = validaTelefone()
                status = "Ativo"
                clientes[cpf_cnpj] = [nome, telefone, email, status]
                arq_clientes = open("clientes.dat", "wb")
                pickle.dump(clientes, arq_clientes)
                arq_clientes.close()
                print()
                print("Cliente cadastrado com sucesso!!!")
                print("Clientes: ", clientes)
                print("\t\t--------------------")
                input("Tecle ENTER para voltar ao menu de clientes...")
                os.system('cls' if os.name == 'nt' else 'clear')
                print()
        
        elif acao == "2":
            print("\t\t  ---EXIBIR DADOS---")
            id = input("Informe o cpf/cnpj do cliente: ")
            print()
            if id in clientes:
              print("\t\t\tDADOS: ")
              print("Nome: ", clientes[id][0])
              print("Telefone: ", clientes[id][1])
              print("Email: ", clientes[id][2])
              print("Status: ", clientes[id][3])
            else:
               print("Cliente não encontrado!")
            print("\t\t-----------------------")
            input("Tecle ENTER para voltar ao menu de clientes...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()

        elif acao == "3":
            print("\t\t---ATUALIZAR DADOS---")
            id = input("Informe o cpf/cnpj do cliente: ")
            print()
            if id in clientes:
               print("\t\t   DADOS ATUAIS: ")
               print("Nome: ", clientes[id][0])
               print("Telefone: ", clientes[id][1])
               print("Email: ", clientes[id][2])
               print("Status: ", clientes[id][3])
               print()
               print("\t\t   DADOS NOVOS: ")
               nome = validaNome()
               telefone = validaTelefone()
               email = validaEmail()
               status = input("Deseja manter o status atual do cliente(S/N)? ")
               if status.lower() == "s":
                   status = clientes[id][3]
               else:
                   if clientes[id][3] == "Ativo":
                       status = "Inativo"
                   else:
                       status = "Ativo"
               clientes[id] = [nome, telefone, email, status]
               arq_clientes = open("clientes.dat", "wb")
               pickle.dump(clientes, arq_clientes)
               arq_clientes.close()
               print()
               print("Cliente atualizado com sucesso!!!")
               print("Clientes: ", clientes)
               print()
            else:
               print("Cliente não encontrado!")
            print("\t\t--------------------")
            input("Tecle ENTER para voltar ao menu de clientes...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()
          
        elif acao == "4":
            print("\t\t---DESATIVAR CLIENTE---")
            id = input("Informe o cpf/cnpj do cliente: ")
            print()
            if id in clientes:
              print("\t\t    DADOS ATUAIS: ")
              print("Nome: ", clientes[id][0])
              print("Telefone: ", clientes[id][1])
              print("Email: ", clientes[id][2])
              print("Status: ", clientes[id][3])
              print()
              confirmacao = input("Deixa excluir(S/N)? ")
              if confirmacao.lower() == "s":
                clientes[id][3] = "Inativo"
                arq_clientes = open("clientes.dat", "wb")
                pickle.dump(clientes, arq_clientes)
                arq_clientes.close()
                print()
                print("Cliente desativado com sucesso!!!")
                print("Clientes: ", clientes)
            else:
               print("Cliente não encontrado!")
            print("\t\t--------------------")
            input("Tecle ENTER para voltar ao menu de clientes...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()

        elif acao == "0":
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        else:
            print("Opção inválida! Escolha uma das opções do menu!")
            print("\t\t--------------------")
            input("Tecle ENTER para voltar ao menu de clientes...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()

  elif op == "2":
    while True:
        print("\t\t---MÓDULO ADVOGADOS---")
        print()
        print("1- Cadastrar Advogado")
        print("2- Visualizar Dados do Advogado")
        print("3- Atualizar Dados do Advogado")
        print("4- Desativar Advogado")
        print("0- Retornar ao Menu Principal")
        print()
        acao = input("Escolha a ação que você deseja realizar: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        print()

        if acao == "1":
            print("\t\t   ---CADASTRAR ADVOGADO---")
            nome = validaNome()
            oab = validaOab()
            if oab in advogados:
                print("Esse advogado já foi cadastrado!!")
                print("\t\t--------------------")
                input("Tecle ENTER para voltar ao menu de advogados...")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                espec = validaEspec()
                telefone = validaTelefone()
                email = validaEmail()
                status = "Ativo"
            advogados[oab] = [nome, espec, telefone, email, status]
            arq_advogados = open("advogados.dat", "wb")
            pickle.dump(advogados, arq_advogados)
            arq_advogados.close()
            print()
            print("Advogado cadastrado com sucesso!!!")
            print("Advogados: ", advogados)
            print()
            print("\t\t---------------------")
            input("Tecle ENTER para voltar ao menu de advogados...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()
        
        elif acao == "2":
            print("\t\t  ---EXIBIR DADOS---")
            id = input("Informe o nº da OAB: ")
            print()
            if id in advogados:
                print("\t\t\tDADOS: ")
                print("Nome: ", advogados[id][0])
                print("Especialidade: ", advogados[id][1])
                print("Telefone: ", advogados[id][2])
                print("Email: ", advogados[id][3])
                print("Status: ", advogados[id][4])
            else:
                print("Advogado não encontrado!")
            print("\t\t---------------------")
            input("Tecle ENTER para voltar ao menu de advogados...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()

        elif acao == "3":
            print("\t\t---ATUALIZAR DADOS---")
            id = input("Informe o nº da OAB: ")
            print()
            if id in advogados:
                print("\t\t   DADOS ATUAIS: ")
                print("Nome: ", advogados[id][0])
                print("Especialidade: ", advogados[id][1])
                print("Telefone: ", advogados[id][2])
                print("Email: ", advogados[id][3])
                print("Status: ", advogados[id][4])
                print()
                print("\t\t   DADOS NOVOS: ")
                nome = validaNome()
                espec = validaEspec()
                telefone = validaTelefone()
                email = validaEmail()
                status = input("Deseja manter o status atual do advogado(S/N)? ")
                if status.lower() == "s":
                   status = advogados[id][4]
                else:
                   if advogados[id][4] == "Ativo":
                       status = "Inativo"
                   else:
                       status = "Ativo"
                advogados[id] = [nome, espec, telefone, email, status]
                arq_advogados = open("advogados.dat", "wb")
                pickle.dump(advogados, arq_advogados)
                arq_advogados.close()
                print()
                print("Advogado atualizado com sucesso!!!")
                print("Advogados: ", advogados)
                print()
            else:
                print("Advogado não encontrado!")
            print("\t\t---------------------")
            input("Tecle ENTER para voltar ao menu de advogados...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()

        elif acao == "4":
            print("\t\t---DESATIVAR ADVOGADO---")
            id = input("Informe o nº da OAB: ")
            print()
            if id in advogados:
                print("\t\t   DADOS ATUAIS: ")
                print("Nome: ", advogados[id][0])
                print("Especialidade: ", advogados[id][1])
                print("Telefone: ", advogados[id][2])
                print("Email: ", advogados[id][3])
                print("Status: ", advogados[id][4])
                print()
                confirmacao = input("Deseja excluir(S/N)? ")
                if confirmacao.lower() == "s":
                    advogados[id][4] = "Inativo"
                    arq_advogados = open("advogados.dat", "wb")
                    pickle.dump(advogados, arq_advogados)
                    arq_advogados.close()
                    print()
                    print("Advogado desativado com sucesso!!!")
                    print("Advogados: ", advogados)
            else:
                print("Advogado não encontrado!")
            print("\t\t---------------------")
            input("Tecle ENTER para voltar ao menu de advogados...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()

        elif acao == "0":
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        else:
            print("Opção inválida! Escolha uma das opções do menu!")
            print("\t\t---------------------")
            input("Tecle ENTER para voltar ao menu de advogados...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()
    
  elif op == "3":
    while True:
        print("\t\t---MÓDULO PROCESSOS---")
        print()
        print("1- Cadastrar Processo")
        print("2- Visualisar Processo")
        print("3- Editar Processo")
        print("4- Desativar Processo")
        print("0- Retornar ao Menu Principal")
        print()
        acao = input("Escolha a ação que você deseja realizar: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        print()

        if acao == "1":
            print("\t\t---CADASTRAR PROCESSO---")
            numero = validaNumero()
            assunto = validaDescricao()
            cliente = input("Cliente (CPF/CNPJ): ")
            if cliente in clientes: 
                if clientes[cliente][3]=="Ativo":
                    cliente = clientes[cliente][0]
                else:
                    print("Cliente não ativado no sistema! Ative o cliente antes de cadastrar o processo!")
                    input("Tecle ENTER para voltar ao menu principal ...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
            else:
               print("Cliente não cadastrado no sistema! Cadastre o cliente antes de cadastrar o processo!")
               input("Tecle ENTER para voltar ao menu principal ...")
               os.system('cls' if os.name == 'nt' else 'clear')
               break
            advogado = input("Advogado responsável (nº da OAB): ")
            if advogado in advogados:
                if advogados[advogado][4]=="Ativo":
                    advogado = advogados[advogado][0]
                else:
                    print("Advogado não ativado no sistema! Ative o advogado antes de abrir o processo!")
                    input("Tecle ENTER para voltar ao menu principal ...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
            else:
               print("Advogado não cadastrado no sistema! Cadastre o advogado antes de abrir o processo!")
               input("Tecle ENTER para voltar ao menu principal ...")
               os.system('cls' if os.name == 'nt' else 'clear')
               break
            data = input("Data do cadastro(XX/YY/XYXY): ")
            status= "Ativo"
            processos[numero] = [assunto, cliente, advogado, data, status]
            arq_processos = open("processos.dat", "wb")
            pickle.dump(processos, arq_processos)
            arq_processos.close
            print()
            print("Processo aberto com sucesso!!!")
            print("Processos: ", processos)
            print("\t\t---------------------")
            input("Tecle ENTER para voltar ao menu de processos...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()
            
        elif acao == "2":
            print("\t\t---VISUALIZAR PROCESSO---")
            id = input("Informe o número do processo: ")
            print()
            if id in processos:
                print("\t\t\tDADOS: ")
                print("Descrição: ", processos[id][0])
                print("Cliente relacionado: ", processos[id][1])
                print("Advogado responsável: ", processos[id][2])
                print("Data do cadastro: ", processos[id][3])
                print("Status: ", processos[id][4])
            else:
                print("Processo não encontrado!Cadastre o processo antes de visualizar!")
            print("\t\t---------------------")
            input("Tecle ENTER para voltar ao menu de processos...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()

        elif acao == "3":
            print("\t\t---ATUALIZAR PROCESSO---")
            id = input("Informe o número do processo: ")
            print()
            if id in processos:
                print("\t\t  DADOS ATUAIS: ")
                print("Descrição: ", processos[id][0])
                print("Cliente relacionado: ", processos[id][1])
                print("Advogado responsável: ", processos[id][2])
                print("Data do cadastro: ", processos[id][3])
                print("Status: ", processos[id][4])
                print()
                print("\t\t  MODIFICAÇÃO: ")
                assunto= validaDescricao()
                advogado= input("Novo advogado(Nº da OAB): ")
                if advogado in advogados:
                    if advogados[advogado][4]=="Ativo":
                        advogado = advogados[advogado][0]
                    else:
                        print("Advogado não ativado no sistema! Ative o advogado antes de abrir o processo!")
                        input("Tecle ENTER para voltar ao menu principal ...")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                else:
                    print("Advogado não cadastrado no sistema! Cadastre o advogado antes de abrir o processo!")
                    input("Tecle ENTER para voltar ao menu principal ...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                status = input("Deseja manter o status atual do processo(S/N)? ")
                if status.lower() == "s":
                   status = processos[id][4]
                else:
                   if processos[id][4] == "Ativo":
                       status = "Encerrado"
                   else:
                       status = "Ativo"
                processos[id] = [assunto,processos[id][1], advogado, processos[id][3], status]
                arq_processos = open("processos.dat", "wb")
                pickle.dump(processos, arq_processos)
                arq_processos.close
                print()
                print("Processo atualizado com sucesso!!!")
                print("Processos: ", processos)
                print()
            else:
                print("Processo não encontrado!")
            print("\t\t---------------------")
            input("Tecle ENTER para voltar ao menu de processos...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()

        elif acao == "4":
            print("\t\t---DESATIVAR PROCESSO---")
            id = input("Informe o número do processo: ")
            print()
            if id in processos:
                print("\t\t   DADOS ATUAIS: ")
                print("Descrição: ", processos[id][0])
                print("Cliente relacionado: ", processos[id][1])
                print("Advogado responsável: ", processos[id][2])
                print("Data do cadastro: ", processos[id][3])
                print("Status: ", processos[id][4])
                print()
                confirmacao = input("Deseja excluir(S/N)? ")
                if confirmacao.lower() == "s":
                    processos[id][4] = "Encerrado"
                    arq_processos = open("processos.dat", "wb")
                    pickle.dump(processos, arq_processos)
                    arq_processos.close
                    print()
                    print("Processo encerrado com sucesso!!!")
                    print("Processos: ", processos)
            else:
                print("Processo não encontrado!")
            print("\t\t---------------------")
            input("Tecle ENTER para voltar ao menu de processos...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()

        elif acao == "0":
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        else:
            print("Opção inválida! Escolha uma das opções do menu!")
            print("\t\t---------------------")
            input("Tecle ENTER para voltar ao menu de processos...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()

  elif op == "4":
    print("\t\t---MÓDULO RELATÓRIOS---")
    print()
    print("1- Lista Geral de Clientes")
    print("2- Lista Geral de Advogados")
    print("3- Lista Geral de Processos")
    print("4- Lista Geral de Clientes p/ Advogado")
    print("5- Lista Geral de Processos p/ Advogado")
    print("0- Retornar ao Menu Principal")
    print()
    acao = int(input("Escolha o que você deseja listar: "))
    print()
    print("###MÓDULO EM DESENVOLVIMENTO###")
    print("----------------------------------------------")
    input("Tecle ENTER para voltar ao menu principal...")
    os.system('cls' if os.name == 'nt' else 'clear')
  
  elif op == "5":
    print("\t\tMÓDULO DE INFORMAÇÕES")
    print()
    print("\t-----------------------------------")
    print("\t| Desenvolvedor(a): Alice Emilly  |")
    print()
    print("\t| Email: a@gmail.com              |")
    print()
    print("\t| Licença Pública Geral GNU       |")  
    print("\t----------------------------------")
    input("Tecle ENTER para voltar ao menu principal...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
  
  elif op == "0":
    print("--------------------------------------------------")
    print("|\t\tPROGRAMA ENCERRADO\t         |")
    print("--------------------------------------------------")
    func = False
  
  else:
    print("Opção inválida! Escolha uma das opções do menu!")
    print("----------------------------------------------")
    input("Tecle ENTER para voltar ao menu principal...")
    os.system('cls' if os.name == 'nt' else 'clear')