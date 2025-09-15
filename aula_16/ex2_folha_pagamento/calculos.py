def calcular_desconto_inss(salario_bruto):
    teto_inss = 114203

    if salario_bruto <= 1518.00:
        desconto = salario_bruto * 0.075
    elif salario_bruto <= 2793.88:
        desconto = salario_bruto * 0.09
    elif salario_bruto <= 4190.83:
        desconto = salario_bruto * 0.12
    elif salario_bruto <= 8157.41:
        desconto = salario_bruto * 0.14
    else:
        desconto = teto_inss

    return desconto

def calcular_desconto_vale_alimentacao(va):
    return va * 0.06

def calcular_desconto_vale_transporte(salario_bruto, vt):
    desconto = salario_bruto * 0.06
    return min(desconto, vt)    




