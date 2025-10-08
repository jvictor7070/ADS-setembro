import os
import time
os.system("cls")

def limpar_tela():
    time.sleep(1.5) # Espera 1.5 segundos.
    print("calculando resultado")
    time.sleep(3) # Espera 1.5 segundos.
    os.system("cls")

# Função com parâmetros e retorno.
def somar(n1, n2):
    soma = n1 + n2
    return soma

# Função com parâmetros e retorno.
def subtrair(n1, n2):
    subtraçao = n1 - n2
    return subtraçao
    
# Função com parâmetros e retorno.
def multiplicar(n1, n2):
    multiplicaçao = n1 * n2
    return multiplicaçao


# Função com parâmetros e retorno.
def dividir(n1, n2):
    divisao = n1 / n2 if n2 != 0 else ("Divisão por 0")
    return divisao

def mostrar_resultados(posiçao1,posiçao2,posiçao3,posiçao4):
    print(f'soma: {posiçao1}')
    print(f'subtração: {posiçao2}')
    print(f'multiplicação: {posiçao3}')
    print(f'divisão: {posiçao4}')

# Código principal
primeiro_numero = int(input(f"Informe o primeiro número: "))
segundo_numero = int(input(f"Informe o segundo número: "))

limpar_tela()

soma = somar(primeiro_numero, segundo_numero)
subtraçao = subtrair(primeiro_numero, segundo_numero)
multiplicaçao = multiplicar(primeiro_numero, segundo_numero)
divisao = dividir(primeiro_numero, segundo_numero)

mostrar_resultados(soma,subtraçao,multiplicaçao,divisao)
