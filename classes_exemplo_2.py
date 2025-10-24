import os
from dataclasses import dataclass
os.system("cls")

# Criando uma classe.
# Cpf? Endereço? nome? Título de eleitor? E-mail? Telefone?
# Seu sitema precisa de algumas informações.
# Uma venda
# Endereço, nome, telefone

@dataclass
class Cliente:
    nome: str
    endereço: str
    telefone: str

# Função apenas dessa classe
    def mostrar_dados_cliente(self):
        print("\n")# Deixando uma lista vazia
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereço}")
        print(f"Telefone: {self.telefone}")
        print("\n")# Deixando uma lista vazia

    # Criando dois clientes com as características.
    # definidas na classe

    # Vetor
lista_de_clientes = []

for i in range(3):
        dados_cliente = Cliente(nome = input("Digite seu nome:"),
                        endereço=input("Digite seu endereço: "),
                        telefone=input("Informe o número do seu telefone: "))      
    
        lista_de_clientes.append(dados_cliente)

# Mostrando os dados do cliente.
for Cliente in lista_de_clientes:
    Cliente.mostrar_dados_cliente()

