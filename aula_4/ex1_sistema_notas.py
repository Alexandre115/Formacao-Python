'''
Sistema para cadastrar os dados de um aluno
'''
def media(nota1,nota2,nota3,nota4):
    resultado = (nota1+nota2+nota3+nota4)/4
    return resultado
def situacao(curriculo_media):
    if curriculo_media >= 7:
        return "Aprovado"
    elif curriculo_media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    turma = input("Digite a turma: ")
    n1 = int(input("Digite a primeira nota: "))   
    n2 = int(input("Digite a segunda nota: "))
    n3 = int(input("Digite a terceira nota: ")) 
    n4 = int(input("Digite a quarta nota: "))

    #Chamar a função media, e armazenar o resultado na variável resultado
    resultado = media(n1,n2,n3,n4)

    print("#"*30)
    print(f"Nome do aluno: {nome}")
    print(f"Turma: {turma}")
    print(f"Notas: {n1}, {n2}, {n3}, {n4}")
    print(f"Média final do aluno: {resultado:.1f}")

    situacao_curricular = situacao(resultado)

    print(f"Situação curricular: {situacao_curricular}")
    print("-"*30)

def main():
    while True: # Criando um loop para cadastrar múltiplos alunos
        print("## Sistema de notas TabajaraCorp ##")
        # Chamar a função para cadastrar um aluno
        cadastrar_aluno()   
        # Perguntar se o usuário deseja cadastrar outro aluno
        continuar = input("Deseja cadastrar outro aluno? (S/N)").lower()

        if continuar != 's':
            print("Cadastro finalizado!")
            break

if __name__ == "__main__":
    main()         