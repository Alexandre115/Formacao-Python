def calcular_desconto_inss(salario_bruto):
    '''
    Função para realizar o calculo do desconto do INSS
    '''
    if salario_bruto <= 1518.00:
        desconto = salario_bruto * 0.075
    elif salario_bruto <= 2793.88:
        desconto = salario_bruto * 0.09
    elif salario_bruto <= 4190.83:
        desconto = salario_bruto * 0.12
    elif salario_bruto <= 8157.41:
        desconto = salario_bruto * 0.14
    else:
        desconto = 908.85

    return desconto

def calcular_desconto_vale_alimentacao(va):
    '''
    Desconto de 6% sobre o valor recebido do vale alimentação
    '''  
    return va * 0.06
def calcular_desconto_vale_transporte(salario_bruto, vt):
    '''
    Função para descontar 6% sobre o salário bruto para 
    vale transporte
    '''  
    desconto = salario_bruto * 0.06
    if desconto > vt:
        desconto = vt
    return desconto

def folha_pagamento():
    while True:
        print("## Sistema de folha de pagamento ##")
        nome = input("Digite o nome do funcionário: ")
        horas_trabalhadas = float(input("Quantidade de horas trabalhadas no mês: "))
        valor_hora = float(input("Digite o valor da hora de trabalho R$ "))
        va = float(input("Digite o valor do vale alimentação R$ "))
        vt = float(input("Digite o valor do vale transporte R$ "))

        salario_bruto = horas_trabalhadas * valor_hora
        desconto_inss = calcular_desconto_inss(salario_bruto) 
        desconto_va = calcular_desconto_vale_alimentacao(va) 
        desconto_vt = calcular_desconto_vale_transporte(salario_bruto, vt)

        salario_liquido = salario_bruto - desconto_inss - desconto_va - desconto_vt

        print("#"*30)
        print("## Folha de pagamento ##")
        print(f"Nome do funcionário: {nome}")
        print(f"Salário bruto R$ {salario_bruto:.2f}")
        print(f"Desconto INSS R$ {desconto_inss:.2f}")
        print(f"Desconto vale alimentação R$ {desconto_va:.2f}")
        print(f"Desconto vale transporte R$ {desconto_vt:.2f}")
        print(f"Vale alimentação recebido R$ {va:.2f}")
        print(f"Vale transporte recebido R$ {vt:.2f}")
        print(f"Salário líquido R$ {salario_liquido:.2f}")
        print("#"*30) 

        # Perguntar se deseja cadastrar um novo funcionário
        novo = input("Deseja cadastrar um novo funcionário (S/N): ").lower()
        if novo != 's':
            print("Encerrando o sistema.")
            break

if __name__ == "__main__":
    folha_pagamento()        
        



