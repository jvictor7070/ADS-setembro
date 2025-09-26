import os
os.system("cls")

print(""""
Código   |   Descrição
   1     | Adicionar familia
   2     | Exibir resultados e Sair
""")



codigo = int(input("Digite seu codigo: "))

match codigo:
    case 1:
        filho = int(input("Quantidade de filhos: "))
        salario = float (input("digite o salario mensal da familia: "))


