import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Usuario:
    nome:str
    idade:int
    peso:float
    altura:float
    def mostrar_dados(self):
        print("Mostrar dados do cliente.")
        print(f"Nome: {self.nome}")
        print(f"Email: {self.idade}")
        print(f"Logradouro: {self.peso}")
        print(f"Número: {self.altura}")

def limpar():
    os.system("cls")

lista_usuarios = []

for i in range(4):
    pessoa = Usuario(nome = input("Informe seu nome: "),
                     idade=input("informe sua idade: "),
                     peso = input("Informe o seu peso: "),
                     altura=input("Informe sua altura: ")
)
    limpar()
    lista_usuarios.append(pessoa)

for pessoa in lista_usuarios:
    pessoa.mostrar_dados()
