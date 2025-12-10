# quando atualizar ou excluir  informar o email ao inves do nome

import os
import time
from dataclasses import dataclass
os.system("cls | | clear") # Limpa o terminal em windows e Linux.

lista_alunos = []

@dataclass
class Endereco:
    logradouro:str
    numero:str
    cidade:str
    estado:str

@dataclass
class Aluno:
    # Atributos da classe.
    # Atributos são variáveis que pertencem à classe.
    nome: str
    data_nascimento:str
    ra:str
    curso:str
    endereco:Endereco


    def mostrar_dados(self):
        print(f"Nome:{self.nome} \nData_nascimento: {self.data_nascimento} \nra: {self.ra} \nCurso: {self.curso} \nlogradouro: {self.endereco.logradouro} \nnumero: {self.endereco.numero} \ncidade: {self.endereco.cidade} \nestado: {self.endereco.estado}")

# Função para verificar se a lista está vazia
def lista_esta_vazia(lista_alunos):
    if not lista_alunos:
        print("\nNâo há Aluno cadastrados.")
        return True
    return False

# Função para adicionar um novo Aluno na lista
def adicionar_Aluno(lista_alunos):
    print("\n--- Adicionar novo Aluno ---")
    nome = input("Digite o seu nome:")
    data_nascimento = input("Digite a sua data_nascimento:")
    ra = input("Digite o seu R.a:")
    curso = input("Digite o nome do seu curso:")
    logradouro = input("Digite o seu logradouro:")
    numero = input("Digite o seu número de residência:")
    cidade = input("Digite a sua cidade de residência:")
    estado = input("Digite o seu estado de residência:")

    novo_Aluno = Aluno(nome=nome,
                       data_nascimento=data_nascimento, 
                       ra=ra, 
                       curso=curso,
                       
   novo_endereco = Endereco(logradouro=logradouro,
                             numero=numero, 
                             cidade=cidade, 
                             estado=estado)
                             )
    
    lista_alunos.append(novo_Aluno)
    print(f"\nAluno {nome} adicionado com sucesso!")

# Função para encontrar um Aluno na lista
def encontrar_aluno_por_nome(lista_alunos, nome_buscar):
    nome_buscar_lower = nome_buscar.lower()
    for aluno in lista_alunos:
        if aluno.nome.lower() == nome_buscar_lower:
            return aluno
    return None #None significa retonar vazio, sem conteudo.

#Função para mostrar todos os Alunos.
def mostrar_todos_alunos(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return
    print("\n--- Lista de Alunos ---")
    for Aluno in lista_alunos:
        print(f"{Aluno.mostrar_dados()}")
 
# Função para atualizar Alunos.
def atualizar_alunos(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return
    
#Mostrar a lista para ajudar o usuario.
def mostrar_todos_alunos(lista_alunos):
    print("--- Atualizar dados de Alunos ---")
    nome_buscar = input("\nDigite o nome do Aluno: ")
    aluno_para_atualizar = encontrar_aluno_por_nome(lista_alunos, nome_buscar)

    if aluno_para_atualizar:
        print("\nAluno encontrado.")
        print("\nDigite os novos dados ou deixe em branco para manter o valor atual.")

        print(f"\nNome atual: { aluno_para_atualizar.nome}")
        novo_nome = input("Novo nome: ")

        print(f"\nData de nascimento atual: {aluno_para_atualizar.data_nascimento}")
        nova_data_aniversario = input("Nova data de nascimento: ")

        print(f"\nR.a atual: { aluno_para_atualizar.ra}")
        novo_ra = input("Novo telefone: ")

        print(f"\Curso atual: { aluno_para_atualizar.curso}")
        novo_curso = input("Novo curso: ")

        print(f"\nLOgradouro atual: {aluno_para_atualizar.logradouro}")
        novo_logradouro = input("Novo logradouro: ")

        print(f"\nNúmero atual: { aluno_para_atualizar.numero}")
        novo_numero = input("Novo número de residência: ")

        print(f"\Cidade atual: {aluno_para_atualizar.cidade}")
        nova_cidade = input("Novo cidade: ")

        print(f"\nEstado atual: { aluno_para_atualizar.estado}")
        novo_estado = input("Novo estado: ")

        if novo_nome:
            aluno_para_atualizar.nome = novo_nome

        if nova_data_aniversario:
            aluno_para_atualizar.data_nascimento = nova_data_aniversario

        if novo_ra:
            aluno_para_atualizar.ra = novo_ra

        if novo_curso:
            aluno_para_atualizar.curso = novo_curso

        if novo_logradouro:
            aluno_para_atualizar.logradouro = novo_logradouro

        if novo_numero:
            aluno_para_atualizar.numero = novo_numero

        if nova_cidade:
            aluno_para_atualizar.cidade = nova_cidade

        if novo_estado:
            aluno_para_atualizar.estado = novo_estado

        print(f"")


def excluir_aluno(lista_aluno):
    if lista_esta_vazia(lista_alunos):
        return
    
    mostrar_todos_alunos(lista_alunos)

    nome_buscar = input("\nDigite o email do Aluno que deseja excluir: ")

    aluno_para_remover = encontrar_aluno_por_nome(lista_alunos, nome_buscar)

    if aluno_para_remover:
        lista_aluno.remove(aluno_para_remover)
        print(f"\nAluno {aluno_para_remover.nome} excluído com sucesso! ")
    else:
        print('\nAluno com o nome {nome_buscar} excluído com sucesso')

    
#MOstrando menu.
while True:
    print("""
          --- Gerenciador de Alunos ---
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
            adicionar_Aluno(lista_alunos)
        case 2:
            mostrar_todos_alunos(lista_alunos)
        case 3:
            atualizar_alunos(lista_alunos)
        case 4:
            excluir_aluno(lista_alunos)
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

    