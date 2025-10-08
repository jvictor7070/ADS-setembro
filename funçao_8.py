# Fazer um programa que solicita o preço de um produto e inflaciona esse preço em 10% se ele for menor que 100 e em 20% se ele for maior ou igual a 100.
# Utilize uma função com retorno para obter o resultado solicitado.

import os
os.system("cls")

def inflacao(preço):
    if preço < 100 :
        preço_inflacionado = preço * 0.10
        aumento = preço + preço_inflacionado
        return aumento 

    if preço >= 100:
        preço_inflacionado = preço * 0.20
        aumento = preço + preço_inflacionado
        return aumento 
    
def mostrar_resultados(resultado):
    print(f"preço reajustado: {resultado}")


    
preço = int(input("Informe o preço do produto: "))  

preço_reajustado = inflacao(preço)

mostrar_resultados(preço_reajustado)




