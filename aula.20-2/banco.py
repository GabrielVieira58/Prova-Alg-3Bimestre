import json
import datetime as dt


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
    conta["saldo"] += valor
    conta["historico"].append(f"Depósito de R$ {valor:.2f}")
    print(f"Depósito realizado com sucesso! Saldo Atual: R$ {conta['saldo']:.2f}")

    
#saque-------------------------------------------------------------------------------------
def sacar(conta, valor):
    if valor <= 0:
        print("O valor do saque deve ser positivo.")
        return
    if valor > conta["saldo"]:
        print("Saldo insuficiente para saque.")
        return
    conta["saldo"] -= valor
    conta["historico"].append(f"Saque de R$ {valor:.2f}")
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
conta = carregar_conta()

if conta is None:
    nome_input = input("Conta não encontrada. Qual seu nome?\nR:  ")
    senha_input = int(input("Digite uma senha com 4 dígitos: "))
    conta = {
        "nome": nome_input,
        "saldo" : 0.0,
        "senha" :  [],
        "historico" : [{
        }]
    }
else:
    print(f"Bem-vindo de volta, {conta['nome']}!")

while True:
    print(f"O que deseja fazer?\nSaldo atual: R${conta['saldo']:.2f}")
    opcao = input("[1] Depositar | [2] Sacar | [3] Extrato | [4] Guardar e Sair: ")
    if opcao == "1" or opcao == "2":
        try:
            valor = float(input("Valor: R$ "))
        except ValueError:
            print("Digite um número válido.")
            continue
        if opcao == "1":
            depositar(conta, valor)

        else: sacar(conta, valor)

    elif opcao == "3":
        extrato(conta)

    elif opcao == "4":
        salvar_conta(conta)
        break

    else:
        print("Opção Inválida!")