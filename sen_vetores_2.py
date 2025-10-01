import os
os.system("cls")

lista_notas = []

for i in range(3):
    nota = int(input(f"Digite a {i+1} nota: "))
    lista_notas.append(nota)

# soma = sum(lista_notas)
media = sum(lista_notas) / i

print("\nResultados:")
for i in range(3):
    print(f"{i+1}ª nota: {lista_notas[i]} ")
# print(f"Soma das notas: {soma}")
print(f"Média: {media}")    
