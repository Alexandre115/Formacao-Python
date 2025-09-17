from aluno import Aluno

def main():
    print("## Sistema escolar ##")
    nome = input("Digite o nome do aluno: ")
    turma = (input("Digite a turma: "))
    n1 = int(input("Digite a primeira nota: "))
    n2 = int(input("Digite a segunda nota: "))
    n3 = int(input("Digite a terceira nota: "))
    n4 = int(input("Digite a quarta nota: "))
    n5 = int(input("Digite a quinta nota: "))

    notas = [n1, n2, n3, n4, n5]

    ''' Vamos instânciar a classe Aluno e enviar os dados para ela'''

    aluno = Aluno(nome, turma, notas)

    media = aluno.calcular_media()
    situacao = aluno.verificar_situacao()

    print("#"*30)
    print(f"Nome do aluno: {nome}")
    print(f"Turma: {turma}")
    print(f"Média do aluno: {media:.1f}")
    print(f"Situação curricular: {situacao}")

if __name__ == "__main__":
    main()    
