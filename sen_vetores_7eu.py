import os
os.system("cls")

# Crie um algoritmo que receba do usuário valores e armazene em um vetor 5 números, caso seja informado um valor negativo, atribua o valor 0.
# Liste os valores do vetor.

numero_vetor = []
positivos = 0
negativos = 0
QUANTIDADE = 5

for i in range(QUANTIDADE):
    numero = int(input(f"Informe o {i+1}º número: "))

    if numero < 0:
       numero = 0
    numero_vetor.append(numero)
    if numero > 0:
        positivos += numero

        


for i, numero in enumerate(numero_vetor, start=1): #star=1 começar com o numero 1 ao inves de zero
    print(f"{i}º digitados: {numero}")
print(f"Soma dos positivos: {positivos}")
print(f"Quantidade de números negativos: {numero}")  