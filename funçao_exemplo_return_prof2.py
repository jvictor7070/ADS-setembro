import os
import time

# Função sem parâmetros e sem retorno.
def limpar_tela():
    time.sleep(3) # Espera 3 segundos.
    os.system("cls")

# Função com parâmetros e com retorno.
def calcular_media(n1, n2):
    calcular = (n1 + n2) / 2
    return calcular

# Função com parâmetros e sem retorno.
def mostrar_resultado(media):
    print(f"Média: {media}")
    time.sleep(2)  
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado") 
         

# Código principal.
# Função sem parâmetros e sem retorno.
limpar_tela() # Chamando a função.

primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite um número: "))

# Função com parâmetros e com retorno.
media = calcular_media(primeiro_numero, segundo_numero)

# Função com parâmetros e sem retorno.
mostrar_resultado(media) # Chamando a função.