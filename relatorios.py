import os
from validacoes import *

def modulo_relatorios(clientes, advogados, processos):
    func = True
    while func:
        print("\t\t---MÓDULO RELATÓRIOS---")
        print()
        print("1- Listagem de Todos os Clientes Ativos")
        print("2- Listagem de Todos os Advogados Ativos")
        print("3- Listagem de Todos os Processos Ativos")
        print("4- Listagem por Filtros ")
        print("0- Retornar ao Menu Principal")
        print()
        acao1 = input("Escolha o que você deseja listar: ").strip()
        os.system('cls' if os.name == 'nt' else 'clear')
    
        if acao1 == "1":
            print(f"{'CPF/CNPJ':^20} | {'NOME':^25} | {'TELEFONE':^20} | {'EMAIL':^15}") 
            print("-" * 90)
            for cpf_cnpj in clientes:
                if clientes[cpf_cnpj][3] == "Ativo":
                    print(f"{cpf_cnpj:<20} | {clientes[cpf_cnpj][0]:<25} | {clientes[cpf_cnpj][1]:<20} | {clientes[cpf_cnpj][2]:<15}")
                    print()
            print()
            input("Tecle ENTER para voltar ao menu de relatórios...")
            os.system('cls' if os.name == 'nt' else 'clear')
        
        elif acao1 == "2":
            print(f"{'OAB':^10} | {'NOME':^25} | {'ESPECIALIDADE':^30} | {'TELEFONE':^20} | {'EMAIL':^15}")
            print("-" * 112)  
            for oab in advogados:
                if advogados[oab][4] == "Ativo":
                    print(f"{oab:<10} | {advogados[oab][0]:<25} | {advogados[oab][1]:<30} | {advogados[oab][2]:<20} | {advogados[oab][3]:<15}")
                    print()
            print()
            input("Tecle ENTER para voltar ao ao menu de relatórios...")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif acao1 == "3":
            print(f"{'CÓDIGO':^10} | {'DESCRIÇÃO':^40} | {'CLIENTE':^25} | {'ADVOGADO':^25} | {'DATA DO PROCESSO':^20}")
            print("-" * 130) 
            for numero in processos:
                if processos[numero][4] == "Ativo":
                    print(f"{numero:<10} | {processos[numero][0]:<40} | {processos[numero][1]:<25} | {processos[numero][2]:<25} | {processos[numero][3]:<20}")
                    print()
            print()
            input("Tecle ENTER para voltar ao menu principal...")
            os.system('cls' if os.name == 'nt' else 'clear')
        
        elif acao1 == "4":
            func2 = True
            while func2:
                print("1) Clientes")
                print("2) Advogados")
                print("3) Processos")
                print("0) Retornar ao Menu de Relatórios ")
                print()
                acao2 = input("Escolha o número do que você deseja listar por filtro: ").strip()
                os.system('cls' if os.name == 'nt' else 'clear')
                
                if acao2 == "1":
                    print("1) Filtrar por Nome/Sobrenome")
                    print("2) Filtrar somente os Clientes Inativos")
                    print()
                    acao3 = input("Informe qual filtro você quer utilizar: ").strip()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print()
                    if acao3 == "1":
                        ns = input("Informe o nome ou sobrenome que você deseja pesquisar: ").strip()
                        totalNomes = 0
                        print("-"*48)
                        for cpf_cnpj in clientes:
                            if ns.lower() in clientes[cpf_cnpj][0].lower(): 
                                print(f"{cpf_cnpj:<15} - {clientes[cpf_cnpj][0]:<25}")
                                totalNomes = totalNomes + 1
                        if totalNomes == 0:
                            print(f"Não há clientes cadastrados com o nome/sobrenome {ns}.")
                        print("-"*48)
                        print()
                        input("Tecle ENTER para voltar ao menu de filtros...")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        
                    elif acao3 == "2":
                        print(f"{'CPF/CNPJ':^20} | {'NOME':^25} | {'TELEFONE':^20} | {'EMAIL':^15}")
                        print("-" * 90)
                        for cpf_cnpj in clientes:
                            if clientes[cpf_cnpj][3] == "Inativo":
                                print(f"{cpf_cnpj:<20} | {clientes[cpf_cnpj][0]:<25} | {clientes[cpf_cnpj][1]:<20} | {clientes[cpf_cnpj][2]:<15}")
                                print()
                        print()
                        input("Tecle ENTER para voltar ao menu de filtros...")
                        os.system('cls' if os.name == 'nt' else 'clear')
                    
                    else:
                        print("Opção inválida! Digite uma das opções do menu!")
                        print("\t\t---------------------")
                        input("Tecle ENTER para voltar ao menu de filtros...")
                        os.system('cls' if os.name == 'nt' else 'clear')

                elif acao2 == "2":
                    print("1) Filtrar por Nome/Sobrenome")
                    print("2) Filtrar pelo Estado da OAB")
                    print("3) Filtrar por Área do Direito")
                    print("4) Filtrar somente os Advogados Inativos")
                    print()
                    acao3 = input("Informe qual filtro você quer utilizar: ").strip()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print()
                    if acao3 == "1":
                        ns = input("Informe o nome ou sobrenome que você deseja pesquisar: ").strip()
                        totalNomes = 0
                        print("-"*40)
                        for oab in advogados:
                            if ns.lower() in advogados[oab][0].lower():
                                print(f"{oab:<9} - {advogados[oab][0]:<25}")
                                totalNomes = totalNomes + 1
                        if totalNomes == 0:
                            print(f"Não há advogados cadastrados com o nome/sobrenome {ns}.")
                        print("-"*40)
                        print()
                        input("Tecle ENTER para voltar ao menu de filtros...")
                        os.system('cls' if os.name == 'nt' else 'clear')
                    
                    elif acao3 == "2":
                        estado = input("Informe a sigla do estado brasileiro que você deseja pesquisar: ").strip()
                        totalEstado = 0
                        print("-"*40)
                        for oab in advogados:
                            n, uf = oab.split("/")  
                            if estado.lower() == uf.lower(): 
                                print(f"{oab:<9} - {advogados[oab][0]:<25}")
                                totalEstado = totalEstado + 1
                        if totalEstado == 0: 
                            print(f"Não há advogados cadastrados com OAB de {estado}.")
                        print("-"*40)
                        print()
                        input("Tecle ENTER para voltar ao menu de filtros...")
                        os.system('cls' if os.name == 'nt' else 'clear')
                    
                    elif acao3 == "3":
                        area = input("Informe a área do direito que você deseja pesquisar: ")
                        totalArea = 0
                        print("-"*40)
                        for oab in advogados:
                            if area.lower() in advogados[oab][1].lower():
                                print(f"{oab:<9} - {advogados[oab][0]:<25}")
                                totalArea = totalArea + 1
                        if totalArea == 0:
                            print(f"Não há advogados cadastrados que atuam no direito {area}.")
                        print("-"*40)
                        print()
                        input("Tecle ENTER para voltar ao menu de filtros...")
                        os.system('cls' if os.name == 'nt' else 'clear')
                       
                    elif acao3 == "4":
                        print(f"{'OAB':^10} | {'NOME':^25} | {'ESPECIALIDADE':^30} | {'TELEFONE':^20} | {'EMAIL':^15}")
                        print("-" * 112) 
                        for oab in advogados:
                            if advogados[oab][4] == "Inativo":
                                print(f"{oab:<10} | {advogados[oab][0]:<25} | {advogados[oab][1]:<30} | {advogados[oab][2]:<20} | {advogados[oab][3]:<15}")
                                print()
                        print()
                        input("Tecle ENTER para voltar ao menu de filtros...")
                        os.system('cls' if os.name == 'nt' else 'clear')
                    
                    else:
                        print("Opção inválida! Digite uma das opções do menu!")
                        print("-" * 47)
                        input("Tecle ENTER para voltar ao menu de filtros...")
                        os.system('cls' if os.name == 'nt' else 'clear')

                elif acao2 == "3":
                    print("1) Filtrar por Cliente")
                    print("2) Filtrar por Advogado")
                    print("3) Filtrar pelo Mês do Processo")
                    print("4) Filtrar somente os Processos Encerrados")
                    print()
                    acao3 = input("Informe qual filtro você quer utilizar: ").strip()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    
                    if acao3 == "1":
                        cpf_cnpj = validaCpf_Cnpj()
                        if cpf_cnpj in clientes:
                            print()
                            print(f"TODOS OS PROCESSOS DO CLIENTE {cpf_cnpj} - {clientes[cpf_cnpj][0]}: ")
                            print()
                            print(f"{'CÓDIGO':^12} | {'DESCRIÇÃO':^40} | {'ADVOGADO':^25} | {'DATA DO PROCESSO':^20} | {'STATUS':^10}")
                            print("-" * 125)
                            totalProcesso = 0
                            for codigo in processos:
                                if clientes[cpf_cnpj][0] == processos[codigo][1]:
                                        print(f"{codigo:<12} | {processos[codigo][0]:<40} | {processos[codigo][2]:<25} | {processos[codigo][3]:<20} |  {processos[codigo][4]:<10}")
                                        totalProcesso = totalProcesso + 1
                            if totalProcesso == 0:
                                print(f"Não há processos cadastrados no cpf/cnpj: {cpf_cnpj}.")
                                print("-" * 100)
                        else:
                            print()
                            print("Cliente não encontrado! Certifique-se de que digitou o CPF/CNPJ da forma exata que está no cadastro.")
                            print("-" * 100)
                        print()
                        input("Tecle ENTER para voltar ao menu de filtros...")
                        os.system('cls' if os.name == 'nt' else 'clear')
  
                    elif acao3 == "2":
                        oab = validaOab()
                        if oab in advogados:
                            print()
                            print(f"TODOS OS PROCESSOS DO ADVOGADO {oab} - {advogados[oab][0]}: ")
                            print()
                            print(f"{'CÓDIGO':^12} | {'DESCRIÇÃO':^40} | {'CLIENTE':^25} | {'DATA DO PROCESSO':^20} | {'STATUS':^10}")
                            print("-" * 125)
                            totalProcesso = 0
                            for codigo in processos:
                                if advogados[oab][0] == processos[codigo][2]:
                                        print(f"{codigo:<12} | {processos[codigo][0]:<40} | {processos[codigo][1]:<25} | {processos[codigo][3]:<20} |  {processos[codigo][4]:<10}")
                                        totalProcesso = totalProcesso + 1
                            if totalProcesso == 0:
                                print(f"Não há processos cadastrados com o acompanhamento do:  {oab}.")
                                print("-" * 100)
                        else:
                            print()
                            print("Advogado não encontrado! Certifique-se de que digitou a OAB da forma exata que está no cadastro.")
                            print("-" * 100)
                        print()
                        input("Tecle ENTER para voltar ao menu de filtros...")
                        os.system('cls' if os.name == 'nt' else 'clear')

                    elif acao3 == "3":
                        print("Informe os meses e os anos dos processos que deseja listar")
                        mesInicio = validaMes("Informe o mês inicial(digite em 2 dígitos): ")
                        anoInicio = validaAno("Informe o ano inicial(digite os 4 dígitos): ")
                        mesFim = validaMes("Informe o mês final(digite em 2 dígitos): ")
                        anoFim = validaAno("Informe o ano final(digite os 4 dígitos): ")
                        while anoInicio>anoFim:
                                print()
                                print("O ano final deve ser posterior ou igual ao ano inicial! Tente novamente")
                                anoFim = validaAno("Informe o ano final(digite os 4 dígitos): ")
                        while anoInicio==anoFim and mesInicio>mesFim:
                            print()
                            print("Quando o ano inicial e o ano final são iguais, o mês inicial deve ser menor que o final")
                            mesInicio = validaMes("Informe o mês inicial(digite em 2 dígitos): ")
                            mesFim = validaMes("Informe o mês final(digite em 2 dígitos): ")

                        inicio = (anoInicio, mesInicio)
                        fim = (anoFim, mesFim)
                        totalProcesso = 0
                        print()
                        print("TODOS OS PROCESSOS ABERTOS ENTRE O PERÍODO INFORMADO: ")
                        print()
                        for codigo in processos:
                            dia, mes, ano = map(int, processos[codigo][3].split('/'))
                            dataProcesso = (ano, mes) 
                            if inicio <= dataProcesso <= fim: 
                                    print(f"{codigo:<10} | {processos[codigo][0]:<40} | {processos[codigo][1]:<25} | {processos[codigo][2]:<25} | {processos[codigo][3]:<15} | {processos[codigo][4]:<10}")
                                    print()
                                    totalProcesso = totalProcesso + 1
                        if totalProcesso == 0: 
                            print(f"Não há processos cadastrados durante o período indicado.")
                            print("-" * 100)
                        print()
                        input("Tecle ENTER para voltar ao menu de filtros...")
                        os.system('cls' if os.name == 'nt' else 'clear')

                    elif acao3 == "4":
                        print(f"{'CÓDIGO':^10} | {'DESCRIÇÃO':^40} | {'CLIENTE':^20} | {'ADVOGADO':^20} | {'DATA DO PROCESSO':^20}")
                        print("-" * 125) 
                        for numero in processos:
                            if processos[numero][4] == "Encerrado":
                                print(f"{numero:<10} | {processos[numero][0]:<40} | {processos[numero][1]:<20} | {processos[numero][2]:<20} | {processos[numero][3]:<20}")
                                print()
                        print()
                        input("Tecle ENTER para voltar ao menu de filtros...")
                        os.system('cls' if os.name == 'nt' else 'clear')

                    else:
                        print("Opção inválida! Digite uma das opções do menu!")
                        print("-" * 47)
                        input("Tecle ENTER para voltar ao menu de filtros...")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print()
                
                elif acao2 == "0":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    func2 = False
                   
                else:
                    print("Opção inválida! Digite uma das opções do menu!")
                    print("-" * 47)
                    input("Tecle ENTER para voltar ao menu de filtros...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print()

        elif acao1 == "0":
            os.system('cls' if os.name == 'nt' else 'clear')
            func = False

        else:
            print("Opção inválida! Digite uma das opções do menu!")
            print("-" * 47)
            input("Tecle ENTER para voltar ao menu de filtros...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print()