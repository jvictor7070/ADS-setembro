import os
import time

os.system("cls")

# Criando uma função


lista_numero = []

# Função sem parametros e sem retorno
def limpar_tela():
    time.sleep(1) #esperar 1 segundos
    os.system("cls")

# Função com parametros e com retorno
def somar(lista_numero):
    return sum(lista_numero)

# Função com parametros e sem retorno
def mostrar_resultado(soma):
    print(f"Resultado: {soma}")

# Código principal.
# Função sem parâmetros e sem retorno.
limpar_tela() # Chamando a função.

for i in range(2):
    numero = float(input("digite um número: "))
    lista_numero.append(numero)

soma = somar(lista_numero)

mostrar_resultado(soma) # chamando função