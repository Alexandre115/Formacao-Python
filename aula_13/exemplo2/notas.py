def media(nota1, nota2, nota3, nota4):
    '''
    Função responsável por receber as notas, e 
    realizar o calculo da média
    '''
    resultado = (nota1 + nota2 + nota3+ nota4) / 4
    return resultado

def situacao(media_notas):
    '''
    Função responsável por verificar a situação 
    curricular do aluno, pela sua média das notas
    '''
    if media_notas >= 7:
        return "Aprovado"
    elif media_notas >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
    
def cadastrar_aluno():
    '''
    Função que solicita os dados de uma aluno e 
    exibe os resultados
    '''    
    nome = input("Digite o nome do aluno: ")
    turma = input("Turma: ")
    n1 = int(input("Digite a primeira nota: "))
    n2 = int(input("Digite a segunda nota: "))
    n3 = int(input("Digite a terceira nota: "))
    n4 = int(input("Digite a quarta nota: "))

    resultado = media(n1,n2,n3,n4)

    print("="*30)
    print(f"Nome do aluno: {nome}")
    print(f"Turma: {turma}")
    print(f"Notas: {n1}, {n2}, {n3}, {n4}")
    print(f"Média escolar: {resultado:.1f}")

    situacao_curricular = situacao(resultado)

    print(f"Situação curricular: {situacao_curricular}")
    print("="*30)

