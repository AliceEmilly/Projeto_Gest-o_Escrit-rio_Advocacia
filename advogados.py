import os 
import pickle
from validacoes import *
from processos import grava_processos

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

def modulo_advogados(advogados,processos):
    while True:
        print("\t\t---MÓDULO ADVOGADOS---")
        print()
        print("1- Cadastrar Advogado")
        print("2- Visualizar Dados do Advogado")
        print("3- Atualizar Dados do Advogado")
        print("4- Ativar/Desativar Advogado")
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
            id = validaOab()
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
            id = validaOab()
            print()
            if id in advogados:
                print("\t\t   DADOS ATUAIS: ")
                print("Nome: ", advogados[id][0])
                print("Especialidade: ", advogados[id][1])
                print("Telefone: ", advogados[id][2])
                print("Email: ", advogados[id][3])
                print("Status: ", advogados[id][4])
                print()
                print("\t\t   MODIFICAÇÃO: ")
                nome = atualizacaoNome(advogados[id][0], validaNome)
                for codigo in processos:
                    if processos[codigo][2] == advogados[id][0] :
                            processos[codigo][2] = nome
                espec = input("Deseja manter a especialidade atual(S/N)? ")
                if espec.lower() == "s":
                   espec = advogados[id][1]
                else:
                    espec = validaEspec()
                telefone = atualizacaoTelefone(advogados[id][2], validaTelefone)
                email = atualizacaoEmail(advogados[id][3], validaEmail)
                advogados[id] = [nome, espec, telefone, email, advogados[id][4]]
                grava_advogados(advogados)
                grava_processos(processos)
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
            print("\t\t---ATIVAR/DESATIVAR ADVOGADO---")
            id = validaOab()
            print()
            if id in advogados:
                print("\t\t   DADOS ATUAIS: ")
                print("Nome: ", advogados[id][0])
                print("Especialidade: ", advogados[id][1])
                print("Telefone: ", advogados[id][2])
                print("Email: ", advogados[id][3])
                print("Status: ", advogados[id][4])
                print()
                if advogados[id][4]  == "Ativo":
                    confirmacao = input("Deseja desativar esse advogado(S/N)? ")
                    if confirmacao.lower() == "s":
                        vinculo = False
                        for codigo in processos:
                            if (processos[codigo][4] == "Ativo") and (advogados[id][0] == processos[codigo][2]):
                                vinculo = True
                        if vinculo:
                            print("Esse advogado está vinculado a um processo em andamento. Encerre o processo ou troque o advogado responsável antes de desativá-lo.")
                        else:
                            advogados[id][4] = "Inativo"
                            grava_advogados(advogados)
                            print()
                            print("Advogado desativado com sucesso!!!")
                else:
                    confirmacao = input("Deseja reativar esse advogado(S/N)? ")
                    if confirmacao.lower() == "s":
                        advogados[id][4] = "Ativo"
                        grava_advogados(advogados)
                        print()
                        print("Advogado reativado com sucesso!!!")
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
            print("Opção inválida! Digite uma das opções do menu!")
            print("\t\t---------------------")
            input("Tecle ENTER para voltar ao menu de advogados...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()