import os

clientes ={
   "111.111.111-11": ["Morticia Addams", "99999-9999", "m@s.gmail.com"],
   "22.222.222/2222-22": ["Empresa X", "77777-7777", "x@empresa.com"],
   "333.333.333-33": ["Fred Flinstone", "66666-6666", "fred@flinstone.com"],
   "00.000.000/0000-00": ["Empresa Y", "88888-8888", "y@empresa.com"]
}

advogados ={
   "123456/RN": ["Saul Goodman", "Direito Criminal","11111-11199", "saul@.gmail.com"],
   "78901/PB": ["Jack McCoy", "Direito Penal", "55555-5555", "jack@gmail.com"],
   "45232/CE": ["Matt Murdock","Direito Civil e Trabalhista", "70707-0707", "matt@gmail.com"],
   "67890/PE": ["Elle Woods","Direito da Família", "34343-4343", "elle@gmail.com"]
}

processos ={
   "0001234-12": ["Ação de Divórcio Litigioso", "111.111.111-11", "123456/RN", "Ativo"],
   "0002847-33": ["Reclamação Trabalhista Rescisória", "22.222.222/2222-22", "45232/CE", "Encerrado"],
   "0005621-07": ["Ação Penal por Homicídio", "333.333.333-33", "78901/PB", "Ativo"]
}

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
  op = int(input("Escolha um número/opção: "))
  os.system('cls' if os.name == 'nt' else 'clear')
  print()
  
  if op == 1:
    while True:
        print("\t\t---MÓDULO CLIENTES---")
        print()
        print("1- Cadastrar Cliente")
        print("2- Exibir Dados do Cliente")
        print("3- Atualizar Dados do Cliente")
        print("4- Remover Cliente")
        print("0- Retornar ao Menu Principal")
        print()
        acao = int(input("Escolha a ação que você deseja realizar: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        
        if acao == 1:
            print("\t\t   ---CADASTRAR---")
            nome = input("Nome Completo(Pessoa/Instituição): ")
            cpf_cnpj = input("CPF/CNPJ: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            clientes[cpf_cnpj] = [nome, telefone, email]
            print()
            print("Cliente cadastrado com sucesso!!!")
            print("Clientes: ", clientes)
            print("\t\t--------------------")
            input("Tecle ENTER para voltar ao menu de clientes...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()
        
        elif acao == 2:
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

        elif acao == 3:
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
              telefoneN = input("Novo telefone: ")
              emailN = input("Novo email: ")
              clientes[id] = [nomeN, telefoneN, emailN]
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
          
        elif acao == 4:
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
                print()
                print("Cliente removido com sucesso!!!")
                print("Clientes: ", clientes)
            else:
               print("Cliente não encontrado!")
            print("\t\t--------------------")
            input("Tecle ENTER para voltar ao menu de clientes...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()

        elif acao == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        else:
            print("Você digitou um número inválido!!!")
            print("Digite um número válido!!!")
            print("\t\t--------------------")
            input("Tecle ENTER para voltar ao menu de clientes...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()

  elif op == 2:
    while True:
        print("\t\t---MÓDULO ADVOGADOS---")
        print()
        print("1- Cadastrar Advogado")
        print("2- Exibir Dados do Advogado")
        print("3- Atualizar Dados do Advogado")
        print("4- Remover Advogado")
        print("0- Retornar ao Menu Principal")
        print()
        acao = int(input("Escolha a ação que você deseja realizar: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        print()

        if acao == 1:
            print("\t\t   ---CADASTRAR---")
            nome = input("Nome Completo: ")
            oab = input("Nº da OAB: ")
            espc = input("Especialidade(Ex.: Trabalhista, Penal, Civil...): ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            print()
            advogados[oab] = [nome, espc, telefone, email]
            print()
            print("Advogado cadastrado com sucesso!!!")
            print("Advogados: ", advogados)
            print()
            print("\t\t---------------------")
            input("Tecle ENTER para voltar ao menu de advogados...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()
        
        elif acao == 2:
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

        elif acao == 3:
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
                espcN = input("Nova especialidade: ")
                telefoneN = input("Novo telefone: ")
                emailN = input("Novo email: ")
                advogados[id] = [nomeN, espcN, telefoneN, emailN]
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

        elif acao == 4:
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
                    print()
                    print("Advogado removido com sucesso!!!")
                    print("Advogados: ", advogados)
            else:
                print("Advogado não encontrado!")
            print("\t\t---------------------")
            input("Tecle ENTER para voltar ao menu de advogados...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()

        elif acao == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        else:
            print("Você digitou um número inválido!!!")
            print("Digite um número válido!!!")
            print("\t\t---------------------")
            input("Tecle ENTER para voltar ao menu de advogados...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()
    
  elif op == 3:
    while True:
        print("\t\t---MÓDULO PROCESSOS---")
        print()
        print("1- Abrir Processo")
        print("2- Visualisar Processo")
        print("3- Editar Processo")
        print("4- Excluir Processo")
        print("0- Retornar ao Menu Principal")
        print()
        acao = int(input("Escolha a ação que você deseja realizar: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        print()

        if acao == 1:
            print("\t\t---ABRIR PROCESSO---")
            numero = input("Número do processo: ")
            assunto = input("Breve descrição: ")
            cliente = input("Cliente (CPF/CNPJ): ")
            advogado = input("Advogado responsável (nº da OAB): ")
            status= "Ativo"
            processos[numero] = [assunto, cliente, advogado, status]
            print()
            print("Processo aberto com sucesso!!!")
            print("Processos: ", processos)
            print("\t\t---------------------")
            input("Tecle ENTER para voltar ao menu de processos...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()
            
        elif acao == 2:
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
                print("Processo não encontrado!")
            print("\t\t---------------------")
            input("Tecle ENTER para voltar ao menu de processos...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()

        elif acao == 3:
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
                advogadoN = input("Novo advogado(Nº da OAB): ")
                statusN = input("Novo status(Encerrado/Ativo): ")
                processos[id] = [assuntoN,processos[id][1], advogadoN, statusN]
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

        elif acao == 4:
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
                    print()
                    print("Processo removido com sucesso!!!")
                    print("Processos: ", processos)
            else:
                print("Processo não encontrado!")
            print("\t\t---------------------")
            input("Tecle ENTER para voltar ao menu de processos...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()

        elif acao == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        else:
            print("Você digitou um número inválido!!!")
            print("Digite um número válido!!!")
            print("\t\t---------------------")
            input("Tecle ENTER para voltar ao menu de processos...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()

  elif op == 4:
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
  
  elif op == 5:
    print("\t\tMÓDULO DE INFORMAÇÕES")
    print()
    print("\t-----------------------------------")
    print("\t| Desenvolvedor(a): Alice Emilly  |")
    print()
    print("\t| Email: a@gmail.com              |")
    print()
    print("\t| Licença:                        |")  
    print("\t----------------------------------")
    input("Tecle ENTER para voltar ao menu principal...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
  
  elif op == 0:
    print("--------------------------------------------------")
    print("|\t\tPROGRAMA ENCERRADO\t         |")
    print("--------------------------------------------------")
    func = False
  
  else:
    print("Você digitou um número inválido!!!")
    print("Digite um número válido!!!")
    print("----------------------------------------------")
    input("Tecle ENTER para voltar ao menu principal...")
    os.system('cls' if os.name == 'nt' else 'clear')