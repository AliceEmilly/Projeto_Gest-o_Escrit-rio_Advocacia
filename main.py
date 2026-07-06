import os
from clientes import *
from advogados import *
from processos import *
from relatorios import *

clientes = recupera_clientes()
advogados = recupera_advogados()
processos = recupera_processos()

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
  op = input("Escolha um número/opção: ").strip()
  os.system('cls' if os.name == 'nt' else 'clear')
  print()
  
  if op == "1":
    modulo_clientes(clientes,processos)
    
  elif op == "2":
    modulo_advogados(advogados,processos)
    
  elif op == "3":
    modulo_processos(processos,clientes,advogados)

  elif op == "4":
    modulo_relatorios(clientes,advogados,processos)
  
  elif op == "5":
    print("\t\tMÓDULO DE INFORMAÇÕES")
    print()
    print("\t-----------------------------------")
    print("\t| Desenvolvedor(a): Alice Emilly  |")
    print()
    print("\t| Email: aliceemilly53@gmail.com  |")
    print()
    print("\t| Licença Pública Geral GNU       |")  
    print("\t-----------------------------------")
    input("Tecle ENTER para voltar ao menu principal...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
  
  elif op == "0":
    print("--------------------------------------------------")
    print("|\t\tPROGRAMA ENCERRADO\t         |")
    print("--------------------------------------------------")
    func = False
  
  else:
    print("Opção inválida! Digite uma das opções do menu!")
    print("----------------------------------------------")
    input("Tecle ENTER para voltar ao menu principal...")
    os.system('cls' if os.name == 'nt' else 'clear')