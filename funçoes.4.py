import os
os.system("cls")

def tabuada(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero *i}")


numero=int(input(f"Informe um número: "))

print("====EXIBINDO RESULTADOS====")
tabuada(numero)

