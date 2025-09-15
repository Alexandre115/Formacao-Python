class Cadastro:
    '''Classe responsável por realizar um cadastro básico de dados 
    de uma pessoa'''

    def __init__(self):
        self.nome = "" # Atributo para armazenar o nome
        self.sobrenome = "" # Atributo para armazenar o sobrenome
        self.idade = 0 # Atributo para armazenar a idade

    def coletar_dados(self):
        '''Método para coletar os dados do usuário através da função 
        input()'''
        print("### Sistema de cadastro de dados ###")
        self.nome = input("Digite o seu nome: ")
        self.sobrenome = input("Digite o seu sobrenome: ")
        self.idade = int(input("Digite a sua idade: "))

    def exibir_dados(self):
        '''Método para exibir os dados cadastrados no console'''
        print("#"*30)
        # Forma moderna de exibir os dados
        print(f"Nome completo: {self.nome} {self.sobrenome}")
        print(f"Idade: {self.idade}") 

        # Forma tradicional de exibir os dados 
        print("Nome completo: ", self.nome, self.sobrenome)
        print("Idade: ",self.idade, "anos")

if __name__ == "__main__":
    cadastro = Cadastro()
    cadastro.coletar_dados()
    cadastro.exibir_dados()              