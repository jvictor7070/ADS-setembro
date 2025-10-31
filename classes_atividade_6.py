import os
os.system("cls")
from dataclasses import dataclass

def limpar():
    os.system("cls")


@dataclass
class Autor:
    nome : str
    biografia:str

@dataclass
class Livro:
    titulo:str
    ano:str
    autor:Autor

    def exibir_detalhes(self):
        print(f"Título do livro: {self.titulo}")
        print(f"Ano de publicação: {self.ano}")
        print(f"Autor: {self.autor.nome}")
        print(f"Biografia: {self.autor.biografia}")



detalhes_obra = Livro(titulo=input("Insira o titulo do livro: "), 
                      ano = input("Qual o ano de publicação: "),
                      autor=Autor(nome=input("Qual o nome do autor: ") ,
                                  biografia=input("Qual a biografia: ")))

limpar()
detalhes_obra.exibir_detalhes()

