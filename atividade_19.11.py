import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Paciente:
    nome:str
    idade:int

    def exibir_dados(self):
        print(f"Nome: {self.nome} n\Idade: {self.idade}")

lista_de_pacientes = []
QUANTIDADE_DE_PACIENTES = 2

for i in range(QUANTIDADE_DE_PACIENTES):
    pacientes = Paciente(
        nome = input("Informe seu nome: "),
        idade= input("Informe sua idade: ")
    )
    lista_de_pacientes.append(pacientes)
    print()#pular uma linha

nome_do_arquivo = "dados_paciente.cvs"
with open(nome_do_arquivo, "a") as arquivo_paciente:
    for paciente in lista_de_pacientes:
        arquivo_paciente.write(f"{paciente.nome}, {paciente.idade}")
        print("Dados salvos com sucesso")

print("n\Exibindo listas de pacienetes")
for paciente in lista_de_pacientes:
    paciente.exibir_dados()


    