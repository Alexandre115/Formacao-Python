'''
Arquivo responsável pela soma das notas, a média e a situação curricular
'''
def media(nota1, nota2, nota3, nota4):
    '''
    Função responsável por receber as notas, realizar a soma e a média. 
    Retornando o resultado do calculo (media das notas digitadas)
    '''
    resultado = (nota1+nota2+nota3+nota4) / 4

    return resultado

def situacao(situacao_curricular):
    '''
    Função responsável por verificar a situação curricular 
    do aluno, através do recebimento da média
    '''
    if situacao_curricular >= 7:
        return "Aprovado"
    elif situacao_curricular >= 5:
        return "Recuperação"
    else:
        return "Reprovado"