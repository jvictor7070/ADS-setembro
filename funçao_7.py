import os
import time
os.system("cls")

def tamanho(metros):
    centimetros = metros * 1000
    print(f"{metros} metros são {centimetros} centimetros.")

def limpar_painel():
    time.sleep(1)
    print("Calculando resultado...")
    time.sleep(3)
    os.system("cls")

metros = int(input("Informe a quantidade de metros: "))

limpar_painel()
tamanho(metros)


