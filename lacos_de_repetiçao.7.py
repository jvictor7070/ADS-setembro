import os
os.system("cls")

soma = 0
contar = 0

while True:
    nota = float (input("Digite sua nota: "))
    contar += 1
    soma += nota 

    continuar = input("gostaria de digitar mais alguma nota?").lower()
    if continuar == "n":
        print("calculando media")
        break

media = soma / contar

print(f"\nmédia: {media}")
