import os 
import pickle  
from validacoes import * 
from processos import grava_processos

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

def modulo_clientes(clientes,processos):
    func = True
    while func: 
        print("\t\t---MÓDULO CLIENTES---") 
        print()
        print("1- Cadastrar Cliente")
        print("2- Visualizar Dados do Cliente")
        print("3- Atualizar Dados do Cliente")
        print("4- Ativar/Desativar Cliente")
        print("0- Retornar ao Menu Principal")
        print()
        acao = input("Escolha a ação que você deseja realizar: ").strip() 
        os.system('cls' if os.name == 'nt' else 'clear') 
        
        if acao == "1":
            print("\t\t   ---CADASTRAR CLIENTE---")
            nome = validaNome()
            cpf_cnpj = validaCpf_Cnpj()
            if cpf_cnpj in clientes: 
                print("Esse cliente já foi cadastrado!!")
                print("--------------------------------")
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
                print("-" * 100)
                input("Tecle ENTER para voltar ao menu de clientes...")
                os.system('cls' if os.name == 'nt' else 'clear')
        
        elif acao == "2":
            print("\t\t  ---EXIBIR DADOS---")
            id = validaCpf_Cnpj()
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

        elif acao == "3":
            print("\t\t---ATUALIZAR DADOS---")
            id = validaCpf_Cnpj()
            print()
            if id in clientes:
               print("\t\t    DADOS ATUAIS: ")
               print("Nome: ", clientes[id][0])
               print("Telefone: ", clientes[id][1])
               print("Email: ", clientes[id][2])
               print("Status: ", clientes[id][3])
               print()
               print("\t\t    MODIFICAÇÃO: ")
               nome = atualizacaoNome(clientes[id][0], validaNome) 
               for codigo in processos: 
                    if clientes[id][0] == processos[codigo][1]:
                            processos[codigo][1] = nome
               telefone = atualizacaoTelefone(clientes[id][1],validaTelefone)
               email = atualizacaoEmail(clientes[id][2],validaEmail)
               clientes[id] = [nome, telefone, email, clientes[id][3]] 
               grava_clientes(clientes)
               grava_processos(processos)
               print()
               print("Cliente atualizado com sucesso!!!")
            else:
               print("Cliente não encontrado! Certifique-se de que digitou o CPF/CNPJ da forma exata que está no cadastro.")
            print("-" * 100)
            input("Tecle ENTER para voltar ao menu de clientes...")
            os.system('cls' if os.name == 'nt' else 'clear')
          
        elif acao == "4":
            print("\t\t---ATIVAR/DESATIVAR CLIENTE---")
            id = validaCpf_Cnpj()
            print()
            if id in clientes:
                print("\t\t      DADOS ATUAIS: ")
                print("Nome: ", clientes[id][0])
                print("Telefone: ", clientes[id][1])
                print("Email: ", clientes[id][2])
                print("Status: ", clientes[id][3])
                print()  
                if clientes[id][3] == "Ativo":
                    confirmacao = input("Deseja desativar esse cliente(S/N)? ")
                    if confirmacao.strip().lower() == "s": 
                        clientes[id][3] = "Inativo"
                        grava_clientes(clientes)
                        totalEncerrados = 0
                        for codigo in processos:
                            if (processos[codigo][4] == "Ativo") and (clientes[id][0] == processos[codigo][1]):
                                processos[codigo][4] = "Encerrado"
                                totalEncerrados = totalEncerrados + 1
                        if totalEncerrados != 0: 
                            grava_processos(processos) 
                            print()
                            print("Cliente desativado. O processo vinculado foi encerrado automaticamente.")
                        else:
                            print()
                            print("Cliente desativado com sucesso!!!")
                else:
                    confirmacao = input("Deseja reativar esse cliente(S/N)? ")  
                    if confirmacao.strip().lower() == "s":
                        clientes[id][3] = "Ativo"
                        grava_clientes(clientes)
                        print()
                        print("Cliente reativado com sucesso!!!")
            else:
               print("Cliente não encontrado! Certifique-se de que digitou o CPF/CNPJ da forma exata que está no cadastro.")
            print("-" * 100)
            input("Tecle ENTER para voltar ao menu de clientes...")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif acao == "0":
            os.system('cls' if os.name == 'nt' else 'clear')
            func = False

        else:
            print("Opção inválida! Digite uma das opções do menu!")
            print("-" * 47)
            input("Tecle ENTER para voltar ao menu de clientes...")
            os.system('cls' if os.name == 'nt' else 'clear')