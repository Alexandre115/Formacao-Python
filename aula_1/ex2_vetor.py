# Sistema de notas utilizando o vetor
print("## Sistema de notas com vetor ##")
nome = input("Digite o nome do aluno: ")
turma = input("Digite a turma do aluno: ")
nota = []
nota.append(int(input("Digite a primeira nota: ")))#nota[0]
nota.append(int(input("Digite a segunda nota: ")))#nota[1]
nota.append(int(input("Digite a terceira nota: ")))#nota[2]
nota.append(int(input("Digite a quarta nota: ")))#nota[3]
nota.append(int(input("Digite a quinta nota: ")))#nota[4]

# Calcular a média das notas
media = sum(nota) / 5
print("#"*30)
print("Nome do aluno: ",nome)
print("Turma: ",turma)
print("Primeira nota: ",nota[0])
print("Segunda nota: ",nota[1])
print("Terceira nota: ",nota[2])
print("Quarta nota: ",nota[3])
print("Quinta nota: ",nota[4])
print("Média final: {:.1f}".format(media))
print(f"Média final: {media:.2f}")