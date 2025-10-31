import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Alunos:
    nome : str
    idade: int
    email:str
    telefone: str

QUANTIDADE_ALUNOS = 2
lista_alunos=[]

print("-----Solicitando dados----")
for i in range(QUANTIDADE_ALUNOS):
    aluno = Alunos(
        nome=input("Informe seu nome: "), idade = input("Informe sua idade:"),
        email=input("informe seu email: "), telefone=input("Informe seu telefone: ")
                   )
    lista_alunos.append(aluno)

print()
print("Salvando os dados")
arquivo = "dados_alunos.txt"


with open(arquivo, "a") as arquivo_dos_alunos:
    for aluno in lista_alunos:
        arquivo_dos_alunos.write(f"{aluno.nome}, {aluno.idade}, {aluno.email}, {aluno.telefone}\n")
        print("Salvo com exito!!!")