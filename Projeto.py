print()
print("--------------------------------------------------")
print("|\tPROJETO AES-ESCRITÓRIO DE ADVOCACIA\t |")
print("--------------------------------------------------")

func = True
while func:
  print()
  print("1) Módulo Cliente")
  print("2) Módulo Advogado")
  print("3) Módulo Agendamentos")
  print("4) Módulo Relatório ")
  print("5) Módulo Informações ")
  print("0) Sair do Programa ")
  print()
  op = int(input("Escolha um número/opção: "))
  print()
  
  if op == 1:
    while True:
        print("\t---MÓDULO CLIENTES---")
        print()
        print("1- Cadastrar Cliente")
        print("2- Exibir Dados do Cliente")
        print("3- Atualizar Dados do Cliente")
        print("4- Remover Cliente")
        print("0- Retornar ao Menu Principal")
        print()
        acao = int(input("Escolha a ação que você deseja realizar: "))
        print()
        
        if acao == 1:
            print("\t---CADASTRAR---")
            nome = input("Nome do cliente: ")
            cpf_cnpj = input("CPF ou CNPJ do cliente: ")
            telefone = input("Telefone do cliente: ")
            email = input("Email do cliente: ")
            endereco = input("Endereço do cliente: ")
            print()
            print("Cliente cadastrado com sucesso!!!")

            print()
            print("---------------------------")
            print("\t OBSERVAÇÃO \t")
            print("As informações colocadas aqui")
            print("ainda não estão sendo salvas!")
            print("----------------------------")
            print()
        
        elif acao == 2:
            print("\t---EXIBIR DADOS---")
            id = input("Informe o cpf ou cnpj do cliente: ")
            print()
            print("\t\tDADOS: ")
            print("CPF/CNPJ: ", id)
            print("Nome: ALICE EMILLY ")
            print("Endereço: Brasil")
            print("Telefone: (83)999999999")
            print("Email: a@gmail.com")

            print()
            print("----------------------------")
            print("\t OBSERVAÇÃO \t")
            print("As informações mostradas aqui")
            print("são simuladas, usadas somente")
            print("para demonstração do módulo! ")
            print("-----------------------------")
            print()

        elif acao == 3:
            print("\t---ATUALIZAR DADOS---")
            id = input("Informe o cpf ou cnpj do cliente: ")
            nomeN = input("Novo nome do cliente: ")
            telefoneN = input("Novo telefone do cliente: ")
            emailN = input("Novo email do cliente: ")
            enderecoN = input("Novo endereço do cliente: ")
            print()
            print("Cliente atualizado com sucesso!!!")

            print()
            print("---------------------------")
            print("\t OBSERVAÇÃO \t")
            print("As informações colocadas aqui")
            print("ainda não estão sendo salvas! ")
            print("----------------------------")
            print()

        elif acao == 4:
            print("\t---REMOVER CLIENTES---")
            id = input("Informe o cpf ou cnpj do cliente: ")
            print()
            print("Cliente removido com sucesso!!!")

            print()
            print("----------------------------")
            print("\t OBSERVAÇÃO \t")
            print("As informações mostradas aqui")
            print("são simuladas, usadas somente")
            print("para demonstração do módulo! ")
            print("-----------------------------")
            print()

        elif acao == 0:
            print("---------------------------")
            print("Você saiu do módulo Clientes")
            print("Escolha outro módulo! ")
            print("----------------------------")
            break

        else:
            print("Você digitou um número inválido!!!")
            print("Digite um número válido!!!")
            print()

  elif op == 2:
    print("\t---MÓDULO ADVOGADOS---")
    print()
    print("1- Cadastrar Advogado")
    print("2- Exibir Dados do Advogado")
    print("3- Atualizar Dados do Advogado")
    print("4- Remover Advogado")
    print("0- Retornar ao Menu Principal")
    print()
    acao = int(input("Escolha a ação que você deseja realizar: "))
    print()
    print("###MÓDULO EM DESENVOLVIMENTO###")
    print("----------------------------------------------")
  
  elif op == 3:
    print("\t---MÓDULO AGENDAMENTOS---")
    print()
    print("1- Agendar")
    print("2- Visualisar Agenda")
    print("3- Reagendar")
    print("4- Cancelar Agendamento")
    print("0- Retornar ao Menu Principal")
    print()
    acao = int(input("Escolha a ação que você deseja realizar: "))
    print()
    print("###MÓDULO EM DESENVOLVIMENTO###")
    print("----------------------------------------------")

  elif op == 4:
    print("\t---MÓDULO RELATÓRIOS---")
    print()
    print("1- Lista Geral de Clientes")
    print("2- Lista Geral de Advogados")
    print("3- Lista Geral de Agendamentos")
    print("4- Lista Geral de Clientes p/ Advogado")
    print("5- Lista Geral de Agendamentos dos Clientes")
    print("0- Retornar ao Menu Principal")
    print()
    acao = int(input("Escolha o que você deseja listar: "))
    print()
    print("###MÓDULO EM DESENVOLVIMENTO###")
    print("----------------------------------------------")
  
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