import json
import datetime as dt
import random


 #21/09
# print(hoje)
# mes_atual = dt.datetime.month #9
# proximo_mes = dt.datetime.__add__3
# print(proximo_mes)

# if hoje == mes_atual:
#     proximo_mes = hoje.month + 1


#Carregar ou criar uma conta

#Carregar conta -------------------------------------------------------------------------
def carregar_conta():
    try:
        with open("conta.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

#Criar conta ----------------------------------------------------------------------------
def salvar_conta(conta):
    try:
        with open("conta.json", "w", encoding="utf-8") as f:
            json.dump(conta, f, ensure_ascii=False, indent=2)
        print("Conta guardada com sucesso!")
    except Exception as e:
        print(f"Erro ao guardar {e}")

        
#Depósito--------------------------------------------------------------------------------
def depositar(conta, valor):
    if valor <= 0:
        print("O valor do depósito deve ser positivo.")
        return
    dia = dt.datetime.day
    now = dt.datetime.today()
    conta["saldo"] += valor
    conta["historico"].append(f"Depósito de R$ {valor:.2f}"), conta["historico"].append(f"Data do depósito: {now}")
    print(f"Depósito realizado com sucesso! Saldo Atual: R$ {conta['saldo']:.2f}")

    
#saque-------------------------------------------------------------------------------------
def sacar(conta, valor):
    if valor <= 0:
        print("O valor do saque deve ser positivo.")
        return
    if valor > conta["saldo"]:
        print("Saldo insuficiente para saque.")
        return
    now = dt.datetime.today()
    conta["saldo"] -= valor
    conta["historico"].append(f"Saque de R$ {valor:.2f}"), conta["historico"].append(f"Data do saque: {now}")
    print(f"Saque realizado com sucesso! Saldo Atual: R$ {conta['saldo']:.2f}")


#Extrato------------------------------------------------------------------------------------
def extrato(conta):
    print(f"\n---EXTRATO DE {conta['nome'].upper()}---")
    if not conta["historico"]:
        print("Nenhuma movimentação realizada ainda...")
    else:
        for movimento in conta["historico"]:
            print(f"- {movimento}")
        print( f"Saldo Atual: R$ {conta['saldo']:.2f}")

#Banco funcionando(Pybank)-------------------------------------------------------------------

print("--- Bem-Vindo ao Pybank ---")


#Aqui foi uma tentativa de fazer um sistema melhor, deixando a opção de criar contas, no entanto não consegui completar, queria que fosse 
# possivel criar várias contas e acessar essas contas com o nome e senha corretos

# usuarios = []

# print("[1] Criar conta | [2] Entrar | [3] Sair")
# op = input("Escolha: ")

# if op == '1':
#     usuario = {}
#     usuario['nome_input'] = input("Conta não encontrada. Qual seu nome?\nR:  ")
#     usuario['senha_input'] = int(input("Digite uma senha com 4 dígitos: "))
#     usuario['saque_max'] = 1000
#     usuario['limite_saque_atual'] = ''
#     usuario['conta'] = {
#         "nome": usuario[nome_input],
#         "saldo" : 0.0,
#         "Saque Máximo" : usuario[saque_max],
#         "Limite Saque Atual" : usuario[limite_saque_atual],
#         "senha" : usuario[senha_input],
#         "historico" : [{
#         }]
#     }
#-----------------------------------------------------------------------------------------------------------

conta = carregar_conta()
if conta is None:
    nome_input = input("Conta não encontrada. Qual seu nome?\nR:  ")
    senha_input = int(input("Digite uma senha com 4 dígitos: "))
    saque_max = 1000
    limite_saque_atual = ''
    conta = {
       "nome": nome_input,
       "saldo" : 0.0,
      "Saque Máximo" : saque_max,
        "Limite Saque Atual" : limite_saque_atual,
        "senha" : senha_input,
        "historico" : [{
        }]
    }
else:
    print(f"Bem-vindo de volta, {conta['nome']}!")
    senha_input = conta['senha']
    saque_max = 1000
    limite_saque_atual = ''
    

while True:
    print(f"O que deseja fazer?\nSaldo atual: R${conta['saldo']:.2f}")
    print(saque_max)
    print(limite_saque_atual)
    opcao = input("[1] Depositar | [2] Sacar | [3] Extrato | [4] Guardar e Sair: ")
    if opcao == "1" or opcao == "2":
        try:
            valor = float(input("Valor: R$ "))
        except ValueError:
            print("Digite um número válido.")
            continue
        if opcao == "1":
            senha_confir = int(input("Digite sua senha para realizar o depósito: "))
            if senha_confir == senha_input:
                depositar(conta, valor)
                senha_confir = 0

            

            else:
                print("Sua senha está incorreta! Tente novamente!")
                senha_confir = 0

        elif opcao == "2" and saque_max > 0 and valor <= saque_max:
            senha_confir = int(input("Digite sua senha para realizar o saque: "))
            if senha_confir == senha_input:
                    sacar(conta, valor)
                    saque_atual = saque_max - valor
                    saque_max = saque_atual

                    senha_confir = 0

            if valor > saque_max:
                print("Seu limite diário de saque já foi excedido!")
            


    elif opcao == "3":
        senha_confir = int(input("Digite sua senha para ver seu extrato: "))
        if senha_confir == senha_input:

            senha_confir = 0
            extrato(conta)
        else:
            print("Sua senha está incorreta! Tente novamente!")
            senha_confir = 0


    elif opcao == "4":
        salvar_conta(conta)
        break

    else:
        print("Opção Inválida!")