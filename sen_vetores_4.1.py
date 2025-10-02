import os
os.system("cls")

lista_numero = []
QUANTINDADE_NUMERO = 5


for i in range(QUANTINDADE_NUMERO):
    numero = int(input(f"Informe a {i+1}º numero: "))
    lista_numero.append(numero)

    maior = max(lista_numero)
    menor = min(lista_numero)

print("\nMostrando Resultado")

for i in range(5):
    print(f"{i+1}ºNúmero: {lista_numero[i]}")    

print(f"maior número: {maior}")    
print(f"menor número: {menor}")    
