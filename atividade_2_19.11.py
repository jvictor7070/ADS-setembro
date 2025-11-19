import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Paciente:
    nome:str
    idade:int
    peso:float
    altura:float
    cpf:str

    def mostrando_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade} \nPeso: {self.peso} \nAltura: {self.altura} \nCpf: {self.cpf}\n")

lista_paciente = []
QUANTIDADE_CLIENTES = 2

for i in range(QUANTIDADE_CLIENTES):
    paciente = Paciente(
        nome = input("Informe o seu nome: "),
        idade = input("Informe o seu idade: "),
        peso = input("Informe o seu peso: "),
        altura = input("Informe o seu altura: "),
        cpf = input("Informe o seu cpf: ")

    )
    lista_paciente.append(paciente)
    print("")

nome_do_arquivo = "informações do paciente.csv"
with open(nome_do_arquivo, "a") as arquivo_paciente:
    for paciente in lista_paciente:
        arquivo_paciente.write(f"{paciente.nome}, {paciente.idade}, {paciente.peso}, {paciente.altura}, {paciente.cpf}\n")
    print("Dados salvos com sucesso")

# print("n\Exibindo listas de pacienetes")
# for paciente in lista_paciente:
#     paciente.mostrando_dados()

# print("\nExibindo todos os pacientes")
# try: #tente
#     #"R" - read - leitura
#     with open(nome_do_arquivo, "r") as arquivo:
#         linhas = arquivo.readlines()
#         for linha in linhas:
#             print(f"- {linha.strip()}")
# except FileNotFoundError: #se não encontrar o arquivo o programa não vai travar.
#     print("O arquivo não foi encontrado.")

# print("\nExibindo todos os pacientes")
# try: #tente
#     #"R" - read - leitura
#     with open(nome_do_arquivo, "r") as arquivo:
#         lista_todos_pacientes = arquivo.readlines()
#         for paciente in lista_todos_pacientes:
#             print(f" {paciente.strip()}")
# except FileNotFoundError: #se não encontrar o arquivo o programa não vai travar.
#     print("O arquivo não foi encontrado.")

print("\nExibindo todos os pacientes")
lista = []

try: #tente
    #"R" - read - leitura
    with open(nome_do_arquivo, "r", encoding="utf-8") as arquivo:
        lista_todos_pacientes = arquivo.readlines()
        for paciente in lista_todos_pacientes:
            nome, idade, peso, altura, cpf = paciente.strip().split(",")
            dados_paciente = Paciente(nome=nome, idade=int(idade), peso=float(peso), altura=float(altura), cpf=str(cpf))
            lista.append(dados_paciente)

    for paciente in lista:
        paciente.mostrando_dados()
except FileNotFoundError: #se não encontrar o arquivo o programa não vai travar.
    print("O arquivo não foi encontrado.")
