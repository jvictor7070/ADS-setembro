import os
os.system("cls")

numeros = []
quantidade_negativos = 0
soma_positivos = 0

for i in range(3):
    numero = int(input(f"digite o {i+1}º número: "))
    numeros.append(numero)
    if numero > 0:
        soma_positivos += numero
    elif numero <0:
        quantidade_negativos +=1

print("\n RESULTADO")
for numero in numeros:
    print(f"Números Digitado: {numero}")
print(f"soma dos números positivos: {soma_positivos}")
print(f"quantidade de números negativos: {quantidade_negativos}")        