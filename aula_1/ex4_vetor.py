print("## Sistema de notas utilizando vetor ##")
nome = input("Digite o nome do aluno: ")
turma = input("Digite a turma: ")
quantidade = int(input("Digite quantas notas deseja informar: "))
nota = []

for i in range(quantidade):
    valor = float(input(f"Digite a {i+1}ª nota: "))
    nota.append(valor)#Adiciona na lista
#medi =(nota[0]+nota[1]+nota[3]) / quantidade
media = sum(nota) / len(nota) 

print("#"*30)
print(f"Nome doa aluno: {nome}")
print(f"Turma: {turma}")

for i in range(quantidade):
    print(f"Nota {i+1}: {nota[i]}")

print(f"Média final do aluno: {media:.2f}")    