import os
os.system("cls")


def positivo_negativo(valor):
    if valor > 0:
        print(f"o número {valor} é: positivo")
    else:
        print(f"o número {valor} é: negativo")

valor = int(input("Informe um valor: "))        

positivo_negativo(valor)