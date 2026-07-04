import os 
import pickle
from validacoes import * 

def recupera_processos():
    try:
        processos= {}
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
        arq_processos.close()
    return processos

def grava_processos(processos):
    arq_processos = open("processos.dat", "wb")
    pickle.dump(processos, arq_processos)
    arq_processos.close()

def modulo_processos(processos,clientes,advogados):
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
            if numero in processos: 
                print("Esse processo já foi cadastrado!!")
                print("\t\t----------------------------")
                input("Tecle ENTER para voltar ao menu de clientes...")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
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
                data = validaData()
                status= "Ativo"
                processos[numero] = [assunto, cliente, advogado, data, status]
                grava_processos(processos)
                print()
                print("Processo aberto com sucesso!!!")
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
                print("Processo não encontrado! Certifique-se de que digitou o código da forma exata que está no cadastro.")
            print("-" * 100)
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
                grava_processos(processos)
                print()
                print("Processo atualizado com sucesso!!!")
                print()
            else:
                print("Processo não encontrado! Certifique-se de que digitou o código da forma exata que está no cadastro.")
            print("-" * 100)
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
                print()
                confirmacao = input("Deseja excluir(S/N)? ")
                if confirmacao.lower() == "s":
                    if processos[id][4] == "Encerrado":
                        print("Esse processo já está encerrado!!")
                    else:
                        processos[id][4] = "Encerrado"
                        grava_processos(processos)
                        print()
                        print("Processo encerrado com sucesso!!!")
            else:
                print("Processo não encontrado! Certifique-se de que digitou o código da forma exata que está no cadastro.")
            print("-" * 100)
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