while True:
    # Exibe o título do sistema
    print("\n## Sistema de notas com vetor ##")

    # Solicita o nome e a turma do aluno
    nome = input("Digite o nome do aluno: ")
    turma = input("Digite a turma: ")

    # Pergunta quantas notas serão informadas
    quantidade = int(input("Quantas notas deseja informar? "))

    nota = []  # Lista para armazenar as notas

    # Coleta as notas
    for i in range(quantidade):
        valor = float(input(f"Digite a {i+1}ª nota: "))
        nota.append(valor)

    # Calcula a média
    media = sum(nota) / len(nota)

    # Exibe o boletim
    print("\n------ Boletim do Aluno ------")
    print("Nome:", nome)
    print("Turma:", turma)
    for i in range(quantidade):
        print(f"Nota {i+1}: {nota[i]}")
    print("Média final: {:.1f}".format(media))

    # Verifica a situação final do aluno
    if media >= 7.0:
        print("Situação: Aprovado")
    elif media >= 5.0:
        print("Situação: Recuperação")
    else:
        print("Situação: Reprovado")

    # Pergunta se o usuário deseja cadastrar outro aluno
    continuar = input("\nDeseja cadastrar outro aluno? (s/n): ").lower()
    if continuar != 's':
        print("\nEncerrando o sistema. Até logo!")
        break