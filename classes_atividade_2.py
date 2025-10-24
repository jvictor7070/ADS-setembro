import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Cliente:
    nome : str
    cpf : str
    telefone : str

    def mostrar_dados(self):
        print("\n")# Deixando uma lista vazia
        print(f"Nome: {self.nome}")
        print(f"cpf: {self.cpf}")
        print(f"Telefone: {self.telefone}")

    def dados_sms_telemarketing(self):    
        print(f"Telefone marketing: {self.telefone}")
        print("\n")# Deixando uma lista vazia


def limpar():
    os.system("cls")
    

lista_clientes = []

for i in range(3):
    dados_do_cliente= Cliente(nome = input("Informe seu nome: "),
                              cpf = input("Informe seu cpf: "),
                              telefone = input("Informe seu número de telefone: "))
    limpar()
    lista_clientes.append(dados_do_cliente)

for cliente in lista_clientes:
    cliente.mostrar_dados()
    cliente.dados_sms_telemarketing()

