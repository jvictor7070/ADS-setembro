import os
os.system("cls")

# Texto que desejo salvar.
texto = input("Digite seu nome: ")

#Definir nome do arquivo a salvar.
nome_arquivo = "exemplo.txt"

#Comando para salvar.
with open(nome_arquivo,"a") as meu_arquivo: #"w" escreve e apaga as informações, "a" acrescenta e mantem as informações
    meu_arquivo.write(f"{texto}\n")
    print("Salvo com sucesso!")
