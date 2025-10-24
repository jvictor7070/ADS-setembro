import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Endereço:
    logradouro: str
    numero: str
    cidade: str

@dataclass
class Pessoa:
    nome : str
    email : str
    endereço : Endereço

    def mostrar_dados(self):
        print("Mostrar dados do cliente.")
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Logradouro: {self.endereço.logradouro}")
        print(f"Número: {self.endereço.numero}")
        print(f"Cidade: {self.endereço.cidade}")

cliente1 = Pessoa(nome = input("Informe seu nome: " ), 
                email = input("Informe seu email: "),
                    endereço = Endereço(logradouro=input("Informe seu lougradouro: "), 
                        numero = input("Informe o número da sua residência: "), 
                        cidade=input("Informe sua cidade: ")))

cliente1.mostrar_dados()