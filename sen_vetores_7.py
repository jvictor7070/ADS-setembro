import os
os.system("cls")

lista_numeros=[]
QUANTIDADE = 5
positivos =[]
negativos=[]


for i in range(QUANTIDADE):
    numero = int(input(f"digite o {i+1}º número: "))
    lista_numeros.append(numero)

    if numero <=0:
        positivos += numero
    else:
        negativos.append(numero)
        


soma_positivo = sum(positivos)

print(f"soma: {soma_positivo}")
