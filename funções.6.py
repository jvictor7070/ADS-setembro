import os
import time
os.system("cls")

def limpar():
    os.system("cls")

lista_notas = []


for i in range(2):
    while True:
        nota = float(input(f"Informe a {i+1}ª nota: "))
        if nota >= 0 and nota <= 10:
            lista_notas.append(nota)
            break
        else:    
            print("nota invalida")
            time.sleep(2)


limpar()

media = sum(lista_notas) / 2

def media():
    media = sum(lista_notas) / 2

    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")   

media()             



