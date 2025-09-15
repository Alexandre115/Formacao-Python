# Função para calcular a média das notas
def media(nota1, nota2, nota3, nota4):
    # Calcula a média das quatro notas
    resultado = (nota1 + nota2 + nota3 + nota4) / 4
    # Retorna o resultado da média
    return resultado

# Função para determinar a situação curricular com base na média
def situacao(curriculo_media):
    # Definindo a situação do aluno com base na média
    if curriculo_media >= 7:
        return "Aprovado"
    elif curriculo_media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

# Função principal que executa o programa
def main():
    # Exibe uma mensagem indicando que o sistema de notas está sendo iniciado
    print("## Sistema de notas utilizando função ##")
    
    # Solicita ao usuário para digitar o nome do aluno
    nome = input("Digite o nome do aluno: ")
    
    # Solicita ao usuário para digitar a turma do aluno
    turma = input("Digite a turma do aluno: ")
    
    # Solicita ao usuário para digitar as notas do aluno
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    n4 = float(input("Digite a quarta nota: "))
    
    # Chama a função 'media' e armazena o resultado na variável 'resultado'
    resultado = media(n1, n2, n3, n4)
    
    # Exibe o nome, turma e a média final do aluno com uma casa decimal
    print(f"\nNome do aluno: {nome}")
    print(f"Turma do aluno: {turma}")
    print(f"Média final do aluno: {resultado:.1f}")
    
    # Chama a função 'situacao' para determinar a situação curricular do aluno
    situacao_curricular = situacao(resultado)
    
    # Exibe a situação curricular do aluno
    print(f"Situação curricular: {situacao_curricular}")

# Executa o programa, chamando a função principal
if __name__ == "__main__":
    main()