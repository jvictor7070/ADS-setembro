import os
os.system("cls")
# criando um vetor

lista_nota = []
# soma = 0

# inserindo notas
for i in range(3):
    nota = int(input(f"Digite a {i+1}ª nota: "))
    lista_nota.append(nota)

# soma += nota
soma = sum(lista_nota)

# # mostra notas:
# print(f"Nota: {lista_nota}")
# print(f"Nota: {lista_nota[0]}") #[] serve pra amostrar uma nota em especifico,começando pelo 0
# # print(F"soma: {soma}")

for i in range(3):
    print(f"{i+1}ª nota: {lista_nota[i]}")
print(f"soma: {soma}")

print("FIM!")    
