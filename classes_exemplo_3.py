from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    endereço:str


# criando dois clientes com sa caractristicas definidas na classe.

cliente1 = Cliente(nome="jojo", endereço="Rua joão")
cliente2 = Cliente(nome="jose", endereço="Rua estrela")

print("\n")# Deixando uma lista vazia
print("Mostrando apenas os nomes do cliente")
print("\n")# Deixando uma lista vazia
print(f"Nome: {cliente1.nome}")
print(f"Nome: {cliente2.nome}")

print("\n")# Deixando uma lista vazia
print("Mostrando apenas os endereços do cliente")
print("\n")# Deixando uma lista vazia
print(f"Endereço: {cliente1.endereço}")
print(f"Endereço: {cliente2.endereço}")

print("\n")# Deixando uma lista vazia
print("Mostrando todos os dados do cliente")
print("\n")# Deixando uma lista vazia
print(f"Nome: {cliente1.nome}")
print(f"Endereço: {cliente1.endereço}\n")
print(f"Nome: {cliente2.nome}")
print(f"Endereço: {cliente2.endereço}\n")