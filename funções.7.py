
# Exercício: Cálculo do Índice de Massa Corpórea (IMC)

# O índice de massa corpórea (IMC) de um indivíduo é obtido dividindo-se o seu peso (em Kg) por sua altura (em metros) ao quadrado.
# Fórmula: IMC = peso / altura²

# Instrução:
# Escreva um programa que solicite ao utilizador o fornecimento do seu peso em kg e de sua altura em m e a partir deles calcule o índice de massa corpórea do utilizador.

# Tabela de Classificação/Recomendação do IMC:
# -------------------------------------------------------------------------------------------------
# | IMC           | Classificação    | Recomendação                                                |
# -------------------------------------------------------------------------------------------------
# | Abaixo de 18.5| Abaixo do peso   | Consulte um nutricionista para orientação                   |
# | 18.5 a 24.9   | Peso normal      | Mantenha hábitos saudáveis!                                 |
# | 25 a 29.9     | Sobrepeso        | Considere uma dieta balanceada e atividade física           |
# | 30 a 34.9     | Obesidade grau 1 | Procure orientação de um profissional de saúde               |
# | 35 a 39.9     | Obesidade grau 2 | Consulte um médico para avaliação e orientação              |
# | 40 ou mais    | Obesidade grau 3 | Busque assistência médica imediatamente                     |
# -------------------------------------------------------------------------------------------------

import os
os.system("cls")

def calcular_imc(peso, altura):
    return peso / (altura * altura)


def situacao(imc):
    if imc >= 40:
        classificacao = "Obesidade grau III"
        recomendacao = "Busque assistência médica imediatamente."
    elif imc >= 35:
        classificacao = "Obesidade grau II"
        recomendacao = "Consulte um médico para avaliação e orientação."
    elif imc >= 30:
        classificacao = "Obesidade grau I"
        recomendacao = "Procure orientação de um profissional de saúde."
    elif imc >= 25:
        classificacao = "Sobrepeso"
        recomendacao = "Considere uma dieta balanceada e atividade física."
    elif imc >= 18.5:
        classificacao = "Peso normal"
        recomendacao = "Mantenha hábitos saudáveis."
    else:
        classificacao = "Abaixo do peso"
        recomendacao = "Consulte um nutricionista para orientação."
    return classificacao, recomendacao

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = calcular_imc(peso, altura)
classificacao, recomendacao = situacao(imc)

print("\n= Exibindo resultados=")
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")
print(f"Recomendação: {recomendacao}")