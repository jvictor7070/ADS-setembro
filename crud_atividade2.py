import os
os.system("cls | | clear") # Limpa o terminal em windows e Linux.
from dataclasses import dataclass
import time

lista_aluno = []

@dataclass
class Endereco:
    logradouro:str
    numero:int
    cidade:str
    estado:str

class Aluno:
    nome:str
    data_nascimento:str
    r_a:str
    curso:str
    endereço:Endereco

    def mostrar_dados(self):
        print(f"Nome: {self.nome} \nNome: {self.data_nascimento} \nR.A: {self.r_a} \nCurso: {self.curso} \nLogradouro: {self.Endereço.logradouro} \nNúmero: {self.Endereço.numero} \nCidade: {self.Endereço.cidade} \nEstado: {self.Endereço.estado}")

def lista_esta_vazia(lista_aluno):
    if not lista_aluno:
        print("\nNâo há alunos cadastrados.")
        return True
    return False

def adicionar_aluno(lista_aluno):
    nome= input("Informe seu nome: ")
    data_nascimento= input("Informe sua data de nascimento: ")
    r_a = input("Informe seu registro de aluno: ")
    curso = input("Informe o seu curso: ")
    logradouro = input("Informe o logradouro de sua residência: ")
    numero = input("Informe o número de sua residência: ")
    cidade = input("Informe a sua cidade: ")
    estado = input("Informe o seu estado : ")

    novo_aluno = Aluno(nome=nome, data_nascimento=data_nascimento, r_a=r_a, curso=curso, logradouro=Aluno.endereço.logradouro, numero=Aluno.endereço.numero, cidade=Aluno.endereço.cidade, estado=Aluno.endereço.estado)
    lista_aluno.append(novo_aluno)
    print(f"Aluno {nome} cadastrado com sucesso.")

def encontrar_aluno_nome(lista_aluno, buscar_nome):
    buscar_nome_lower = buscar_nome.lower
    for aluno in lista_aluno:
        if aluno.nome.lower() == buscar_nome.lower:
            return aluno
        return None
    
def mostrar_todos_alunos(lista_aluno):
    if lista_esta_vazia(lista_aluno):
        return
    print("LIsta de alunos")
    for aluno in lista_aluno:
        print(f"{aluno.mostrar_dados()}")

def atualizar_aluno(lista_aluno):
    if lista_esta_vazia(lista_aluno):
        return
    
def mostrar_todos_os_alunos(lista_aluno):
    print("--- Atualizar dados de alunos ---")
    buscar_nome = input("\n DIgite o nome do aluno: ")
    atualizar_aluno = encontrar_aluno_nome(lista_aluno, buscar_nome)

    if atualizar_aluno(lista_aluno):
        print("\nPessoa encontrada.")
        print("\nDigite os novos dados ou deixe em branco para manter o valor atual.")

        print(f"\nNome atual: {atualizar_aluno.nome}")
        novo_nome = input("novo nome: ")

        print(f"\nCurso atual: {atualizar_aluno.curso}")
        novo_curso = input("novo curso: ")
        
        print(f"\nLogradouro atual: {atualizar_aluno.logradouro}")
        novo_logradouro = input("novo nome: ")

        print(f"\nNúmero atual: {atualizar_aluno.numero}")
        novo_numero = input("novo número: ")

        print(f"\nCidade atual: {atualizar_aluno.cidade}")
        novo_cidade = input("nova cidade: ")

        print(f"\nEstado atual: {atualizar_aluno.estado}")
        novo_estado = input("novo eatado: ")

        if novo_nome:
            atualizar_aluno.nome = novo_nome

        if novo_curso:
            atualizar_aluno.curso = novo_curso
            
        if novo_logradouro:
            atualizar_aluno.logradouro = novo_logradouro

        if novo_numero:
            atualizar_aluno.numero = novo_numero

        if novo_cidade:
            atualizar_aluno.cidade = novo_cidade

        if novo_estado:
            atualizar_aluno.estado = novo_estado

        print(f"cadastro do aluno {novo_nome} atualizado.")

def excluir_alunos(lista_aluno):
    if lista_esta_vazia(lista_aluno):
        return
    
    mostrar_todos_os_alunos(lista_aluno)

    buscar_nome = input("\nbusque pelo nome do aluno")
    aluno_para_remover = input("\n Digite o nome do aluno que deseja remover:")

    if aluno_para_remover:
        lista_aluno.remove = encontrar_aluno_nome
        print(f"\nAluno {aluno_para_remover.email} excluído com sucesso! ")
    else:
        print('\naluno com o nome {buscar_nome} excluído com sucesso')
    
while True:
    print("""
          --- Gerenciador de alunos ---
          1 - Adicionar
          2 - Mostrar todos
          3 - Atualizar
          4 - Excluir
          0 - Sair
          """)
    try:
        opçao = int(input ("Digite uma das opções acima: "))
    except ValueError:
        print("\nEntrada inválida. Digite um número...")
        time.sleep(2)
        os.system("cls || clear")
        continue
    
    match opçao:
        case 1:
            adicionar_aluno(lista_aluno)
        case 2:
            mostrar_todos_alunos(lista_aluno)
        case 3:
            atualizar_aluno(lista_aluno)
        case 4:
            excluir_alunos(lista_aluno)
        case 0:
            print("\nSaindo do programa...")
            break
        case _:
            print("\nOpção inválida. \nTente novamente. ")
    if opçao !=1 and opçao !=0:
        time.sleep(3)
    elif opçao == 1:
        time.sleep(1)

#Limpar tela
    if opçao !=0:
        os.system("cls || clear")

