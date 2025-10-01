import os
os.system("cls")

lista_notas = []
QUANTIDADE_DE_NOTAS = 4

for i in range(QUANTIDADE_DE_NOTAS):
    notas = float(input(f"informe a {i+1}ª nota: "))
    lista_notas.append(notas)

media = sum(lista_notas) / i

if media >= 7:
    resultado = "Aprovado"
elif media >= 5:
    resultado = "Recuperação"
else:        
    resultado = "Reprovado"


for i in range(QUANTIDADE_DE_NOTAS):
    print(f"{i+1}ª nota: {lista_notas[i]} ")
print(f"\nMedia: {media:.2f}")
print(f"Resultado: {resultado}")


    