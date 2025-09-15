# Definindo a classe Cadastro
class Cadastro:
    """
    Classe responsável por armazenar e gerenciar os dados de cadastro de um usuário.
    """

    def __init__(self):
        """
        Método construtor da classe.
        Inicializa todos os atributos necessários para o cadastro como strings vazias ou zero.
        'self' representa a própria instância do objeto.
        """
        self.nome = ""        # Nome do usuário
        self.sobrenome = ""   # Sobrenome do usuário
        self.idade = 0        # Idade do usuário
        self.endereco = ""    # Endereço (rua, avenida, etc.)
        self.bairro = ""      # Bairro
        self.cidade = ""      # Cidade
        self.uf = ""          # Estado (UF)
        self.telefone = ""    # Número de telefone
        self.email = ""       # Endereço de e-mail
        self.rg = ""          # Número do RG
        self.cpf = ""         # Número do CPF

    def coletar_dados(self):
        """
        Método que coleta os dados do usuário através do console, utilizando input().
        A idade é convertida de string para inteiro.
        """
        print("### Sistema de cadastro Tabajara ###")  # Título do sistema

        # Coletando os dados do usuário
        self.nome = input("Digite o seu nome: ")                   # Nome
        self.sobrenome = input("Digite o seu sobrenome: ")         # Sobrenome
        self.idade = int(input("Digite a sua idade: "))            # Idade (convertido para inteiro)
        self.endereco = input("Digite o seu endereço: ")           # Endereço
        self.bairro = input("Digite o seu bairro: ")               # Bairro
        self.cidade = input("Digite a sua cidade: ")               # Cidade
        self.uf = input("Digite o seu estado (UF): ")              # Estado
        self.telefone = input("Digite o seu telefone: ")           # Telefone
        self.email = input("Digite o seu e-mail: ")                # E-mail
        self.rg = input("Digite o seu RG: ")                       # RG
        self.cpf = input("Digite o seu CPF: ")                     # CPF

    def exibir_dados(self):
        """
        Método que exibe os dados cadastrados no console de forma organizada e formatada.
        """
        print("######################################")
        print("## Dados informados pelo usuário ##")
        print("######################################")

        # Exibindo o nome completo
        print(f"Nome completo: {self.nome} {self.sobrenome}")

        # Exibindo endereço completo
        print(f"Endereço completo: {self.endereco}, Bairro: {self.bairro}, "
              f"Cidade: {self.cidade}, Estado: {self.uf}")

        # Exibindo os demais dados
        print(f"Telefone: {self.telefone}")
        print(f"E-mail: {self.email}")
        print(f"RG: {self.rg}")
        print(f"CPF: {self.cpf}")


# Bloco principal do programa
if __name__ == "__main__":
    # Criando um objeto da classe Cadastro
    cadastro = Cadastro()

    # Chamando o método para coletar dados
    cadastro.coletar_dados()

    # Chamando o método para exibir os dados
    cadastro.exibir_dados()
