import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Endereço:
    logradouro:str
    numero:int

@dataclass
class Pessoa:
    nome : str
    idade : int
    endereço : Endereço #RElacionando com a classe Endereço


pessoa = Pessoa(nome = input("Informe seu nome: "), idade = input("Informe sua idade: "),
                endereço = Endereço(logradouro=input("informe seu logradouro: "), numero = input("Informe o número da sua residência: ")                     
                
                ))


print("Mostrar dados do cliente.")
print(f"Nome: {pessoa.nome}")
print(f"Nome: {pessoa.idade}")
print(f"Logradouro: {pessoa.endereço.logradouro}")
print(f"Número: {pessoa.endereço.numero}")