import os
os.system("cls")

# Função com passagem de parâmetros.
# Criando Função
def saudacao(nome, idade, peso, altura):
    print(f"Olá, {nome}! Bem-vindo(a)!")
    print(f"Sua idade é {idade} anos")
    print(f"Seu peso é {peso} kg")
    print(f"Sua altura é {altura} metros")

def sumido():
    os.system("cls")  
    print("\nSolicitando dados")

sumido()   
nome = input("digite seu nome: ")    
sumido()
idade = int(input("Digite sua idade: "))
sumido()

peso = float(input("Digite sua peso: "))
sumido()

altura = float(input("Digite sua altura: "))

# Chamando a função.
saudacao(nome, idade, peso, altura)