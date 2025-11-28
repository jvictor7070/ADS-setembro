# quando atualizar ou excluir  informar o email ao inves do nome

import os
import time
from dataclasses import dataclass
os.system("cls | | clear") # Limpa o terminal em windows e Linux.

lista_clientes = []

@dataclass
class Cliente:
    # Atributos da classe.
    # Atributos são variáveis que pertencem à classe.
    nome: str
    email:str
    telefone:str

    def mostrar_dados(self):
        print(f"Nome:{self.nome} \nE-mail: {self.email} \nTelefone: {self.telefone}")

# Função para verificar se a lista está vazia
def lista_esta_vazia(lista_clientes):
    if not lista_clientes:
        print("\nNâo há cliente cadastrados.")
        return True
    return False

# Função para adicionar um novo cliente na lista
def adicionar_cliente(lista_clientes):
    print("\n--- Adicionar novo cliente ---")
    nome = input("Digite seu nome:")
    email = input("Digite seu email:")
    telefone = input("Digite seu telefone:")

    novo_cliente = Cliente(nome=nome, email=email, telefone=telefone)
    lista_clientes.append(novo_cliente)
    print(f"\nCliente {nome} adicionado com sucesso!")

# Função para encontrar um cliente na lista
def encontrar_cliente_por_email(lista_clientes, email_buscar):
    email_buscar_lower = email_buscar.lower()
    for cliente in lista_clientes:
        if cliente.email.lower() == email_buscar_lower:
            return cliente
    return None #None significa retonar vazio, sem conteudo.

#Função para mostrar todos os clientes.
def mostrar_todos_clientes(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
    print("\n--- Lista de clientes ---")
    for cliente in lista_clientes:
        print(f"{cliente.mostrar_dados()}")
 
# Função para atualizar clientes.
def atualizar_clientes(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
    
#Mostrar a lista para ajudar o usuario.
def mostrar_todos_clientes(lista_clientes):
    print("--- Atualizar dados de clientes ---")
    email_buscar = input("\nDigite o nome do cliente: ")
    cliente_para_atualizar = encontrar_cliente_por_email(lista_clientes, email_buscar)

    if cliente_para_atualizar:
        print("\nPessoa encontrada.")
        print("\nDigite os novos dados ou deixe em branco para manter o valor atual.")

        print(f"\nNome atual: { cliente_para_atualizar.nome}")
        novo_nome = input("Novo nome: ")

        print(f"\nEmail: atual: {cliente_para_atualizar.email}")
        novo_email = input("Novo email: ")

        print(f"\ntelefone atual: { cliente_para_atualizar.telefone}")
        novo_telefone = input("Novo telefone: ")

        if novo_nome:
            cliente_para_atualizar.nome = novo_nome

        if novo_email:
            cliente_para_atualizar.email = novo_nome

        if novo_telefone:
            cliente_para_atualizar.telefone = novo_nome

        print(f"")


def excluir_cliente(lista_cliente):
    if lista_esta_vazia(lista_clientes):
        return
    
    mostrar_todos_clientes(lista_clientes)

    email_buscar = input("\nDigite o email do cliente que deseja excluir: ")

    cliente_para_remover = encontrar_cliente_por_email(lista_clientes, email_buscar)

    if cliente_para_remover:
        lista_cliente.remove(cliente_para_remover)
        print(f"\nCliente {cliente_para_remover.email} excluído com sucesso! ")
    else:
        print('\nCliente com o nome {email_buscar} excluído com sucesso')

    
#MOstrando menu.
while True:
    print("""
          --- Gerenciador de Clientes ---
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
            adicionar_cliente(lista_clientes)
        case 2:
            mostrar_todos_clientes(lista_clientes)
        case 3:
            atualizar_clientes(lista_clientes)
        case 4:
            excluir_cliente(lista_clientes)
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

    