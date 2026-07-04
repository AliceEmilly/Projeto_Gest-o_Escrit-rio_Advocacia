import os 
import pickle
from validacoes import * 

def recupera_clientes():
    try:
        clientes= {}
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
        arq_clientes.close()
    return clientes

def grava_clientes(clientes):
    arq_clientes = open("clientes.dat", "wb")
    pickle.dump(clientes, arq_clientes)
    arq_clientes.close()

def modulo_clientes(clientes):
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
                grava_clientes(clientes)
                print()
                print("Cliente cadastrado com sucesso!!!")
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
               print("Cliente não encontrado! Certifique-se de que digitou o CPF/CNPJ da forma exata que está no cadastro.")
            print("-" * 100)
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
               grava_clientes(clientes)
               print()
               print("Cliente atualizado com sucesso!!!")
               print()
            else:
               print("Cliente não encontrado! Certifique-se de que digitou o CPF/CNPJ da forma exata que está no cadastro.")
            print("-" * 100)
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
              print()
              confirmacao = input("Deixa excluir(S/N)? ")
              if confirmacao.lower() == "s":
                if clientes[id][3] == "Inativo":
                        print("Esse cliente já está inativo!!")
                else:
                    clientes[id][3] = "Inativo"
                    grava_clientes(clientes)
                    print()
                    print("Cliente desativado com sucesso!!!")
            else:
               print("Cliente não encontrado! Certifique-se de que digitou o CPF/CNPJ da forma exata que está no cadastro.")
            print("-" * 100)
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
