import os
os.system("cls")

lista_numero = []
quantidade_de_numeros = 6

pares = 0
impares = 0

for i in range(quantidade_de_numeros):
    numeros = int(input(f"digite o {i+1}º número: "))
    lista_numero.append (numeros)

    if numeros % 2 == 0:
        pares += 1
    else:
        impares += 1

# for i in range(quantidade_de_numeros):
#     print(f"numeros:{lista_numero[i]}")

# for(foreach)=para cada
for numeros in lista_numero:
    print(f"Número: {numeros}")


print(f"Números pares: {pares}")    
print(f"Números impares: {impares}")    
