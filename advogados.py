import os 
import pickle
from validacoes import *

def recupera_advogados():
    try:
        advogados= {}
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
        arq_advogados.close()
    return advogados 

def grava_advogados(advogados):
    arq_advogados = open("advogados.dat", "wb")
    pickle.dump(advogados, arq_advogados)
    arq_advogados.close()

def modulo_advogados(advogados):
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
            grava_advogados(advogados)
            print()
            print("Advogado cadastrado com sucesso!!!")
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
                print("Advogado não encontrado! Certifique-se de que digitou a OAB da forma exata que está no cadastro.")
            print("-" * 100)
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
                grava_advogados(advogados)
                print()
                print("Advogado atualizado com sucesso!!!")
                print()
            else:
                print("Advogado não encontrado! Certifique-se de que digitou a OAB da forma exata que está no cadastro.")
            print("-" * 100)
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
                print()
                confirmacao = input("Deseja excluir(S/N)? ")
                if confirmacao.lower() == "s":
                    if (advogados[id][4] == "Inativo"):
                            print("Esse advogado já está inativo!!")
                    else:
                        advogados[id][4] = "Inativo"
                        grava_advogados(advogados)
                        print()
                        print("Advogado desativado com sucesso!!!")
            else:
                print("Advogado não encontrado! Certifique-se de que digitou a OAB da forma exata que está no cadastro.")
            print("-" * 100)
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