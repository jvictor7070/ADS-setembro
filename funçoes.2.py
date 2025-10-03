import os
os.system("cls")


def parimpar(numero):

    if numero %2 == 0 :
        print(f"O número {numero} é: par") 
    else:
        print(f"O número {numero} é: impar") 

numero = int(input("Informe um número:")) 
pares = 0
impares = 0

parimpar(numero)
  