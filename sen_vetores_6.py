import os
os.system("cls")

print("""
Código\tPrato\t\tPreço
1\tPicanha\t\tR$25,00
2\tLasanha\t\tR$20,00
3\tStrogonoff\tR$18,00
4\tBife Acebolado\tR$15,00
5\tPão com ovo\tR$5,00

""")

pedido = input("digite o código do seu pedido: ")
vetor = []

vetor.append(pedido)

for cardapio in vetor:

    while True:
        print("digite N(não) ou S(sim)")
        mais_pedidos= input("gostaria de pedir mais algum prato:")

        if mais_pedidos == "s":
            pedido = input("digite o código do seu pedido: ")
            break
        else:
            

            

