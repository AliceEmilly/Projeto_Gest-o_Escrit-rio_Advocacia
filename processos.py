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
        print("3- Atualizar Processo")
        print("4- Ativar/Encerrar Processo")
        print("0- Retornar ao Menu Principal")
        print()
        acao = input("Escolha a ação que você deseja realizar: ").strip()
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
                cliente = validaCpf_Cnpj()
                if cliente in clientes: 
                    if clientes[cliente][3] == "Ativo":
                        cliente = clientes[cliente][0]
                    else:
                        print()
                        print("Cliente não ativado no sistema! Ative o cliente antes de cadastrar o processo!")
                        input("Tecle ENTER para voltar ao menu principal ...")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                else:
                    print()
                    print("Cliente não cadastrado no sistema! Cadastre o cliente antes de cadastrar o processo!")
                    input("Tecle ENTER para voltar ao menu principal ...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                #nesse caso o código verifica se existe aquele cliente no dicionário cliente, se sim, ele verifica se tá ativo, se não tiver manda ativar e volta pro menu principal
                #caso o cliente não esteja cadastrado o mesmo acontece. Caso ele esteja ativo e cadastrado, a variável cliente vai guardar o nome associado aquela chave que foi digitada
                advogado = validaOab()
                if advogado in advogados:
                    if advogados[advogado][4] == "Ativo":
                        advogado = advogados[advogado][0]
                    else:
                        print()
                        print("Advogado não ativado no sistema! Ative o advogado antes de abrir o processo!")
                        input("Tecle ENTER para voltar ao menu principal ...")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                else:
                    print()
                    print("Advogado não cadastrado no sistema! Cadastre o advogado antes de abrir o processo!")
                    input("Tecle ENTER para voltar ao menu principal ...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                data = validaData()
                status = "Ativo"
                processos[numero] = [assunto, cliente, advogado, data, status]
                grava_processos(processos)
                print()
                print("Processo cadastrado com sucesso!!!")
                print("-" * 100)
                input("Tecle ENTER para voltar ao menu de processos...")
                os.system('cls' if os.name == 'nt' else 'clear')
                print()
            
        elif acao == "2":
            print("\t\t---VISUALIZAR PROCESSO---")
            id = validaNumero()
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
            id = validaNumero()
            print()
            if id in processos:
                print("\t\t    DADOS ATUAIS: ")
                print("Descrição: ", processos[id][0])
                print("Cliente relacionado: ", processos[id][1])
                print("Advogado responsável: ", processos[id][2])
                print("Data do cadastro: ", processos[id][3])
                print("Status: ", processos[id][4])
                print()
                print("\t\t    MODIFICAÇÃO: ")
                desc = input("Deseja manter a descrição atual(S/N)? ") 
                if desc.strip().lower() == "s":
                    desc = processos[id][0]
                else:
                    print()
                    desc = validaDescricao()
                advogado = input("Deseja manter o advogado atual(S/N)? ") 
                if advogado.strip().lower() == "s":
                    advogado = processos[id][2]
                else:
                    print()
                    oab = validaOab()
                    if oab in advogados:
                        if advogados[oab][4] == "Ativo":
                            advogado = advogados[oab][0]
                        else:
                            print()
                            print("Advogado não ativado no sistema! Ative o advogado antes de abrir o processo!")
                            input("Tecle ENTER para voltar ao menu principal ...")
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break
                    else:
                        print()
                        print("Advogado não cadastrado no sistema! Cadastre o advogado antes de abrir o processo!")
                        input("Tecle ENTER para voltar ao menu principal ...")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    #faz a mesma verificação de antes
                processos[id] = [desc,processos[id][1], advogado, processos[id][3], processos[id][4]] #nesse caso vai manter tanto o cliente, quanto a data e o satus do processo
                grava_processos(processos)
                print()
                print("Processo atualizado com sucesso!!!")
            else:
                print()
                print("Processo não encontrado! Certifique-se de que digitou o código da forma exata que está no cadastro.")
            print("-" * 100)
            input("Tecle ENTER para voltar ao menu de processos...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()

        elif acao == "4":
            print("\t\t---ATIVAR/ENCERRAR PROCESSO---")
            id = validaNumero()
            print()
            if id in processos:
                print("\t\t       DADOS ATUAIS: ")
                print("Descrição: ", processos[id][0])
                print("Cliente relacionado: ", processos[id][1])
                print("Advogado responsável: ", processos[id][2])
                print("Data do cadastro: ", processos[id][3])
                print()
                if processos[id][4] == "Ativo":
                    confirmacao = input("Deseja encerrar esse processo(S/N)? ")
                    if confirmacao.strip().lower() == "s":
                        processos[id][4] = "Encerrado"
                        grava_processos(processos)
                        print()
                        print("Processo encerrado com sucesso!!!")
                else:
                    confirmacao = input("Deseja reativar esse processo(S/N)? ")
                    if confirmacao.strip().lower() == "s":
                        cliente_ativo = False
                        for cpf_cnpj in clientes:
                            if (clientes[cpf_cnpj][3] == "Ativo") and (clientes[cpf_cnpj][0] == processos[id][1]):
                                cliente_ativo = True
                        advogado_ativo = False
                        for oab in advogados:
                            if (advogados[oab][4] == "Ativo") and (advogados[oab][0] == processos[id][2]):
                                advogado_ativo = True
                        if not cliente_ativo:
                            print("Não foi possível reativar: o cliente vinculado a esse processo está inativo no sistema.")
                        elif not advogado_ativo:
                            print("Não foi possível reativar: o advogado vinculado a esse processo está inativo no sistema.")
                        else:
                            processos[id][4] = "Ativo"
                            grava_processos(processos)
                            print()
                            print("Processo reativado com sucesso!!!")
                    #nesse caso nós temos que verificar se o cliente e o advogado estão ativos, se pelo menos um deles não estiver, o processso não pode ser reativado
                    #se cliente_ativo/advogado_ativo = True, não entra nem no if nem no elif, mas se for igual a False, ja que tem not na frente da condição, ela acaba ficando true e entra no bloco, aparecendo a mensagem refrente e não deixando ativar o processo
            else:
                print()
                print("Processo não encontrado! Certifique-se de que digitou o código da forma exata que está no cadastro.")
            print("-" * 100)
            input("Tecle ENTER para voltar ao menu de processos...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()

        elif acao == "0":
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        else:
            print("Opção inválida! Digite uma das opções do menu!")
            print("\t\t---------------------")
            input("Tecle ENTER para voltar ao menu de processos...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()