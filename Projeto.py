import os
import pickle

#clientes ={
#   "111.111.111-11": ["Morticia Addams", "(99)99999-9999", "m@s.gmail.com"],
#   "22.222.222/2222-22": ["Empresa X", "(77)77777-7777", "x@empresa.com"],
#   "333.333.333-33": ["Fred Flinstone", "(66)66666-6666", "fred@flinstone.com"],
#   "00.000.000/0000-00": ["Empresa Y", "(88)88888-8888", "y@empresa.com"]
#}

#advogados ={
#   "123456/RN": ["Saul Goodman", "Direito Criminal","(11)11119-1199", "saul@.gmail.com"],
#   "78901/PB": ["Jack McCoy", "Direito Penal", "(55)55555-5555", "jack@gmail.com"],
#   "45232/CE": ["Matt Murdock","Direito Civil e Trabalhista", "(70)70707-0707", "matt@gmail.com"],
#   "67890/PE": ["Elle Woods","Direito da Família", "(43)34343-4343", "elle@gmail.com"]
#}

#processos ={
#   "0001234-12": ["Ação de Divórcio Litigioso", "111.111.111-11", "123456/RN", "Ativo"],
#   "0002847-33": ["Reclamação Trabalhista Rescisória", "22.222.222/2222-22", "45232/CE", "Encerrado"],
#   "0005621-07": ["Ação Penal por Homicídio", "333.333.333-33", "78901/PB", "Ativo"]
#}

try:
    arq = open("clientes.dat", "rb")
    clientes = pickle.load(arq)
    arq.close()
except:
    clientes = {}

try:
    arq = open("advogados.dat", "rb")
    advogados = pickle.load(arq)
    arq.close()
except:
    advogados = {}

try:
    arq = open("processos.dat", "rb")
    processos = pickle.load(arq)
    arq.close()
except:
    processos = {}

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
        print("4- Remover Cliente")
        print("0- Retornar ao Menu Principal")
        print()
        acao = input("Escolha a ação que você deseja realizar: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        
        if acao == "1":
            print("\t\t   ---CADASTRAR---")
            nome = input("Nome Completo (Pessoa/Organização): ")
            nome.strip()
            while nome == "":
               print("Você esqueceu de digitar o nome! Tente novamente!")
               print()
               nome = input("Nome Completo (Pessoa/Organização): ")
            
            cpf_cnpj = input("CPF/CNPJ: ")
            while cpf_cnpj == "":
               print("Você esqueceu de digitar o cpf/cnpj! Tente novamente!")
               print()
               cpf_cnpj = input("CPF/CNPJ: ")
            cpf_cnpj_s = cpf_cnpj.replace(".", "").replace("-", "").replace("/", "")
            while (not( cpf_cnpj_s.isnumeric()) or (len(cpf_cnpj_s) != 11 and len(cpf_cnpj_s) != 14)):
               print("Houve algum erro ao digitar o cpf/cnpj! Tente novamente!")
               print("Atenção: o CPF deve conter 14 caracteres (incluindo pontos e traço) e o CNPJ 18 caracteres (incluindo pontos, traço e barra).")
               print()
               cpf_cnpj = input("CPF/CNPJ: ")
               cpf_cnpj_s = cpf_cnpj.replace(".", "").replace("-", "").replace("/", "")

            telefone = input("Telefone: ")
            while telefone == "":
               print("Você esqueceu de digitar o telefone! Tente novamente!")
               print()
               telefone = input("Telefone: ")
            telefone_s = telefone.replace("(", "").replace(")", "").replace("-", "")
            while not((telefone_s.isnumeric()) and (len(telefone_s) == 10 or len(telefone_s) == 11)):
               print("Houve algum erro ao digitar o telefone! Tente novamente!")
               print("Atenção: o telefone deve conter apenas números, com 10 ou 11 dígitos.")
               print()
               telefone = input("Telefone: ")
               telefone_s = telefone.replace("(", "").replace(")", "").replace("-", "")

            email = input("Email: ")
            while email == "":
               print("Você esqueceu de digitar o email! Tente novamente!")
               print()
               email = input("Email: ")
            while (email.count("@") != 1 or email.count(".") == 0):
               print("Houve algum erro ao digitar o email! Tente novamente!")
               print("Atenção: o e-mail deve conter exatamente um '@' e pelo menos um ponto (.).")
               print()
               email = input("Email: ")

            clientes[cpf_cnpj] = [nome, telefone, email]
            arq = open("clientes.dat", "wb")
            pickle.dump(clientes, arq)
            arq.close()

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
               print()
               print("\t\t   DADOS NOVOS: ")
               nomeN = input("Novo nome: ")
               nomeN.strip()
               while nomeN == "":
                print("Você esqueceu de digitar o novo nome! Tente novamente!")
                print()
                nomeN = input("Novo nome: ")

               telefoneN = input("Novo telefone: ")
               while telefoneN == "":
                    print("Você esqueceu de digitar o novo telefone! Tente novamente!")
                    print()
                    telefoneN = input("Novo telefone: ")
               telefoneN_s = telefoneN.replace("(", "").replace(")", "").replace("-", "")
               while not((telefoneN_s.isnumeric()) and (len(telefoneN_s) == 10 or len(telefoneN_s) == 11)):
                    print("Houve algum erro ao digitar o novo telefone! Tente novamente!")
                    print("Atenção: o telefone deve conter apenas números, com 10 ou 11 dígitos.")
                    print()
                    telefoneN = input("Novo telefone: ")
                    telefoneN_s = telefoneN.replace("(", "").replace(")", "").replace("-", "")

               emailN = input("Novo email: ")
               while emailN == "":
                    print("Você esqueceu de digitar o novo email! Tente novamente!")
                    print()
                    emailN = input("Novo email: ")
               while (emailN.count("@") != 1 or emailN.count(".") == 0):
                    print("Houve algum erro ao digitar o novo email! Tente novamente!")
                    print("Atenção: o e-mail deve conter exatamente um '@' e pelo menos um ponto (.).")
                    print()
                    emailN = input("Novo email: ")

               clientes[id] = [nomeN, telefoneN, emailN]
               arq = open("clientes.dat", "wb")
               pickle.dump(clientes, arq)
               arq.close()
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
            print("\t\t---REMOVER CLIENTES---")
            id = input("Informe o cpf/cnpj do cliente: ")
            print()
            if id in clientes:
              print("\t\t    DADOS ATUAIS: ")
              print("Nome: ", clientes[id][0])
              print("Telefone: ", clientes[id][1])
              print("Email: ", clientes[id][2])
              print()
              confirmacao = input("Deixa excluir(S/N)? ")
              if confirmacao.lower() == "s":
                del clientes[id]
                arq = open("clientes.dat", "wb")
                pickle.dump(clientes, arq)
                arq.close()
                print()
                print("Cliente removido com sucesso!!!")
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
        print("4- Remover Advogado")
        print("0- Retornar ao Menu Principal")
        print()
        acao = input("Escolha a ação que você deseja realizar: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        print()

        if acao == "1":
            print("\t\t   ---CADASTRAR---")
            nome = input("Nome Completo: ")
            nome.strip()
            while nome == "":
               print("Você esqueceu de digitar o nome! Tente novamente!")
               print()
               nome = input("Nome Completo: ")
        
            oab = input("Nº da OAB(formato NNNNNN/UF): ")
            while oab == "":
               print("Você esqueceu de digitar o nº da OAB! Tente novamente!")
               print()
               oab = input("Nº da OAB: ")
            while oab.count("/") != 1:
                print("Houve algum erro ao digitar o nº da OAB! Tente novamente!")
                print("Atenção: a OAB deve seguir o formato NNNNNN/UF, com até 6 números seguidos antes da barra e a sigla do estado após.")
                print()
                oab = input("Nº da OAB: ")
            numero, uf = oab.split("/")
            while (not numero.isnumeric()) or (len(uf) != 2 or not(uf.isalpha())):
                print("Houve algum erro ao digitar o nº da OAB! Tente novamente!")
                print("Atenção: a OAB deve seguir o formato NNNNNN/UF, com até 6 números seguidos antes da barra e a sigla do estado após.")
                print()
                oab = input("Nº da OAB: ")
                numero, uf = oab.split("/")

            espec = input("Especialidade(Ex.: Trabalhista, Penal, Civil...): ")
            while espec == "":
               print("Você esqueceu de digitar a especialidade! Tente novamente!")
               print()
               espec = input("Especialidade: ")

            telefone = input("Telefone: ")
            while telefone == "":
               print("Você esqueceu de digitar o telefone! Tente novamente!")
               print()
               telefone = input("Telefone: ")
            telefone_s = telefone.replace("(", "").replace(")", "").replace("-", "")
            while not((telefone_s.isnumeric()) and (len(telefone_s) == 10 or len(telefone_s) == 11)):
               print("Houve algum erro ao digitar seu telefone! Tente novamente!")
               print("Atenção: o telefone deve conter apenas números, com 10 ou 11 dígitos.")
               print()
               telefone = input("Telefone: ")
               telefone_s = telefone.replace("(", "").replace(")", "").replace("-", "")

            email = input("Email: ")
            while email == "":
               print("Você esqueceu de digitar o email! Tente novamente!")
               print()
               email = input("Email: ")
            while (email.count("@") != 1 or email.count(".") == 0):
               print("Houve algum erro ao digitar seu email! Tente novamente!")
               print("Atenção: o e-mail deve conter exatamente um '@' e pelo menos um ponto (.).")
               print()
               email = input("Email: ")

            print()
            advogados[oab] = [nome, espec, telefone, email]
            arq = open("advogados.dat", "wb")
            pickle.dump(advogados, arq)
            arq.close()
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
                print()
                print("\t\t   DADOS NOVOS: ")
                nomeN = input("Novo nome: ")
                while nomeN == "":
                    print("Você esqueceu de digitar o nome! Tente novamente!")
                    print()
                    nomeN = input("Novo nome: ")
        
                especN = input("Nova especialidade: ")
                while especN == "":
                    print("Você esqueceu de digitar a nova especialidade! Tente novamente!")
                    print()
                    especN = input("Nova especialidade: ")
               
                telefoneN = input("Novo telefone: ")
                while telefoneN == "":
                    print("Você esqueceu de digitar o novo telefone! Tente novamente!")
                    print()
                    telefoneN = input("Telefone: ")
                telefoneN_s = telefoneN.replace("(", "").replace(")", "").replace("-", "")
                while not((telefoneN_s.isnumeric()) and (len(telefoneN_s) == 10 or len(telefoneN_s) == 11)):
                    print("Houve algum erro ao digitar o novo telefone! Tente novamente!")
                    print("Atenção: o telefone deve conter apenas números, com 10 ou 11 dígitos.")
                    print()
                    telefoneN = input("Telefone: ")
                    telefoneN_s = telefoneN.replace("(", "").replace(")", "").replace("-", "")

                emailN = input("Novo email: ")
                while emailN == "":
                    print("Você esqueceu de digitar o novo email! Tente novamente!")
                    print()
                    emailN = input("Email: ")
                while (emailN.count("@") != 1 or emailN.count(".") == 0):
                    print("Houve algum erro ao digitar o novo email! Tente novamente!")
                    print("Atenção: o e-mail deve conter exatamente um '@' e pelo menos um ponto (.).")
                    print()
                    emailN = input("Novo email: ")

                advogados[id] = [nomeN, especN, telefoneN, emailN]
                arq = open("advogados.dat", "wb")
                pickle.dump(advogados, arq)
                arq.close()
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
            print("\t\t---REMOVER CLIENTES---")
            id = input("Informe o nº da OAB: ")
            print()
            if id in advogados:
                print("\t\t   DADOS ATUAIS: ")
                print("Nome: ", advogados[id][0])
                print("Especialidade: ", advogados[id][1])
                print("Telefone: ", advogados[id][2])
                print("Email: ", advogados[id][3])
                print()
                confirmacao = input("Deseja excluir(S/N)? ")
                if confirmacao.lower() == "s":
                    del advogados[id]
                    arq = open("advogados.dat", "wb")
                    pickle.dump(advogados, arq)
                    arq.close()
                    print()
                    print("Advogado removido com sucesso!!!")
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
        print("4- Excluir Processo")
        print("0- Retornar ao Menu Principal")
        print()
        acao = input("Escolha a ação que você deseja realizar: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        print()

        if acao == "1":
            print("\t\t---CADASTRAR PROCESSO---")
            numero = input("Número do processo(informe os primeiros nove dígitos): ")
            while numero == "":
                    print("Você esqueceu de digitar o número do processo! Tente novamente!")
                    print()
                    numero = input("Número do processo: ")
            numero_s = numero.replace("-", "")
            while not(numero_s.isnumeric()) or (len(numero_s) != 9):
                    print("Houve algum erro ao digitar o número do processo! Tente novamente!")
                    print("Atenção: o número do processo deve conter apenas números, com 9 dígitos.")
                    print()
                    numero = input("Número do processo: ")
                    numero_s = numero.replace("-", "")

            assunto = input("Breve descrição: ")
            while assunto == "":
                    print("Você esqueceu de digitar a descrição!Tente novamente!")
                    print()
                    assunto = input("Descrição: ")

            cliente = input("Cliente (CPF/CNPJ): ")
            if cliente in clientes:
                cliente = clientes[cliente][0]
            else:
               print("Cliente não cadastrado no sistema! Cadastre o cliente antes de abrir o processo!")
               input("Tecle ENTER para voltar ao menu principal ...")
               os.system('cls' if os.name == 'nt' else 'clear')
               break

            advogado = input("Advogado responsável (nº da OAB): ")
            if advogado in advogados:
                advogado = advogados[advogado][0]
            else:
               print("Advogado não cadastrado no sistema! Cadastre o advogado antes de abrir o processo!")
               input("Tecle ENTER para voltar ao menu principal ...")
               os.system('cls' if os.name == 'nt' else 'clear')
               break

            status= "Ativo"
            processos[numero] = [assunto, cliente, advogado, status]
            arq = open("processos.dat", "wb")
            pickle.dump(processos, arq)
            arq.close
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
                print("Status: ", processos[id][3])
            else:
                print("Processo não encontrado!Cadastre o processo antes de visualizar!")
            print("\t\t---------------------")
            input("Tecle ENTER para voltar ao menu de processos...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()

        elif acao == "3":
            print("\t\t---EDITAR PROCESSO---")
            id = input("Informe o número do processo: ")
            print()
            if id in processos:
                print("\t\t  DADOS ATUAIS: ")
                print("Descrição: ", processos[id][0])
                print("Cliente relacionado: ", processos[id][1])
                print("Advogado responsável: ", processos[id][2])
                print("Status: ", processos[id][3])
                print()
                print("\t\t  MODIFICAÇÃO: ")
                assuntoN = input("Nova descrição: ")
                while assuntoN == "":
                    print("Você esqueceu de digitar a nova descrição!Tente novamente!")
                    print()
                    assuntoN = input("Nova descrição: ")

                advogadoN = input("Novo advogado(Nº da OAB): ")
                if advogadoN in advogados:
                    advogadoN = advogados[advogadoN][0]
                else:
                    print("Advogado não cadastrado no sistema!")
                    input("Tecle ENTER para voltar ao menu principal ...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break

                statusN = input("Novo status(Encerrado/Ativo): ")
                while statusN == "":
                    print("Você esqueceu de digitar o novo status!Tente novamente!")
                    print()
                    statusN = input("Novo status: ")

                processos[id] = [assuntoN,processos[id][1], advogadoN, statusN]
                arq = open("processos.dat", "wb")
                pickle.dump(processos, arq)
                arq.close
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
            print("\t\t---EXCLUIR PROCESSO---")
            id = input("Informe o número do processo: ")
            print()
            if id in processos:
                print("\t\t   DADOS ATUAIS: ")
                print("Descrição: ", processos[id][0])
                print("Cliente relacionado: ", processos[id][1])
                print("Advogado responsável: ", processos[id][2])
                print("Status: ", processos[id][3])
                print()
                confirmacao = input("Deseja excluir(S/N)? ")
                if confirmacao.lower() == "s":
                    del processos[id]
                    arq = open("processos.dat", "wb")
                    pickle.dump(processos, arq)
                    arq.close
                    print()
                    print("Processo removido com sucesso!!!")
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