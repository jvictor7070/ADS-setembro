from dataclasses import dataclass

@dataclass
class Endereço:
    logradouro: str
    numero: int

@dataclass
class Cliente:
    nome: str
    endereço: Endereço

cliente1 = Cliente(nome="Marta",
                   endereço = Endereço(logradouro="Rua A",numero="123") )

print("Mostrar dados do cliente.")
print(f"Nome: {cliente1.nome}")
print(f"Endereço: {cliente1.endereço.logradouro}")
print(f"Número: {cliente1.endereço.numero}")
