import os
os.system("cls")
from dataclasses import dataclass

# Implemente um programa que leia as informações de 3 livros com os seguintes dados:
# Nome
# Autor
# Categoria
# Preço
# Salve os dados dos livros em um arquivo chamado: catalogo_livros.txt

@dataclass
class Livro:
    nome:str
    autor:str
    categoria:str
    preço:int

livro_informaçoes = Livro(nome=input("Informe o nome do livro: "),
                          autor=input("Informe o nome do autor: "),
                          categoria=input("Informe a categoria do livro: "),
                          preço=input("Informe o preço do livro: ")     
                          )

arquivo="Catalogo_livros.txt"

with open (arquivo, "a") as arquivos_livro:
    arquivos_livro.write(f"{livro_informaçoes.nome}, {livro_informaçoes.autor}, {livro_informaçoes.categoria}, {livro_informaçoes.preço}\n")
    print("Salvo com sucesso!!!")