from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    cpf:str

@dataclass
class Pet:
    nome: str
    idade: int
    peso: float

# Exemplo de uso da classe.
# Nota: A classe 'Pessoa' não está definida neste trecho, mas é instanciada.
pessoa1 = Pessoa("Marta", 20, "123.456.789-00")
pet1 = Pet("Totó", 4, 15.6)

print("Exibindo dados da Pessoa.")
# Exibe Nome e Idade de pessoa1. O '\n' no final adiciona uma linha em branco.
print(f"Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}\ncpf: {pessoa1.cpf} ") 

print("Exibindo dados do Pet.")
# Exibe Nome e Idade de pet1.
print(f"Nome: {pet1.nome}\nIdade: {pet1.idade}\npeso: {pet1.peso}")

# --------------------------------------------------------------------------------

# Explicação:

# 1. 'from dataclasses import dataclass':
#    - Esta linha importa o decorador 'dataclass' do módulo padrão 'dataclasses' do Python.
#    - Dataclasses são classes que são usadas principalmente para armazenar dados (como um contêiner de dados) e minimizam a necessidade de escrever métodos repetitivos.

# 2. '@dataclass':
#    - Este é um 'decorador' aplicado à classe 'Pessoa'.
#    - Ele automaticamente gera métodos especiais ('dunder methods') essenciais para classes de dados, incluindo:
#      - '__init__': Construtor para inicializar os atributos (nome e idade).
#      - '__repr__': Método para criar uma representação de string útil e legível da classe.
#      - '__eq__': Método para permitir a comparação entre instâncias.

# 3. 'class Pessoa: nome: str idade: int':
#    - Define a classe 'Pessoa' com dois atributos tipados:
#      - 'nome': do tipo string ('str').
#      - 'idade': do tipo inteiro ('int').
#    - Graças ao decorador '@dataclass', não é necessário escrever o método '__init__', pois ele é gerado automaticamente usando estes atributos.

# 4. '# Exemplo de uso da classe':
#    - 'pessoa1 = Pessoa("Alice", 30)': Cria uma nova instância da classe 'Pessoa', passando 'Alice' para 'nome' e '30' para 'idade'.
#    - 'pessoa2 = Pessoa("Bob", 25)': Cria uma segunda instância.

# 5. 'print(...)':
#    - As duas linhas 'print' exibem os valores dos atributos das instâncias usando *f-strings* (string formatada literal).
#    - O acesso aos atributos é feito de maneira padrão: 'pessoa1.nome' e 'pessoa1.idade'.

# Em resumo, este código demonstra o uso conciso das **Dataclasses** em Python para criar classes de modelo de dados com menos código repetitivo, facilitando a criação de objetos.
# """