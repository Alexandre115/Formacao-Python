class Aluno:
    def __init__(self):
        self.nome = ""
        self.turma = ""
        self.n1 = 0
        self.n2 = 0
        self.n3 = 0
        self.n4 = 0
        self.n5 = 0
        self.media = 0.0

    def coletar_dados(self):
        print("## Sistema de notas ##")
        self.nome = input("Digite o nome do aluno: ")
        self.turma = input("Turma: ")
        self.n1 = int(input("Digite a primeira nota: "))  
        self.n2 = int(input("Digite a segunda nota: ")) 
        self.n3 = int(input("Digite a terceira nota: ")) 
        self.n4 = int(input("Digite a quarta nota: "))
        self.n5 = int(input("Digite a quinta nota: "))

    def calcular_media(self):
        self.media = (self.n1+self.n2+self.n3+self.n4+self.n5) / 5

    def exibir_dados(self):
        print("#"*30)
        print(f"Nome do aluno: {self.nome}") 
        print(f"Turma: {self.turma}")
        print(f"Notas: {self.n1}, {self.n2}, {self.n3}, {self.n4}, {self.n5}")
        print(f"Média final: {self.media:.2f}")
        print("Média final: {:.2f}".format(self.media))
        print("Média final: %.2f"% self.media)

if __name__ == "__main__":
    aluno = Aluno()
    aluno.coletar_dados()
    aluno.calcular_media()
    aluno.exibir_dados()               