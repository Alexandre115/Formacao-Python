from calculos import (
    calcular_desconto_inss,
    calcular_desconto_vale_alimentacao,
    calcular_desconto_vale_transporte
)
from arquivo import salvar_folha_em_arquivo
from utils import ler_float, ler_str

def folha_pagamento():
    while True:
        print("\n#### Sistema de folha de pagamento ####\n")
        nome = ler_str("Nome do funcionário: ")
        horas_trabalhadas = ler_float("Horas trabalhadas no mês: ")
        valor_hora = ler_float("Valor da hora R$ ")
        va = ler_float("Valor do vale alimentação R$ ")
        vt = ler_float("Valor do vale transporte R$ ")

        salario_bruto = horas_trabalhadas * valor_hora
        desconto_inss = calcular_desconto_inss(salario_bruto)
        desconto_va = calcular_desconto_vale_alimentacao(va)
        desconto_vt = calcular_desconto_vale_transporte(salario_bruto, vt)

        salario_liquido = salario_bruto - desconto_inss - desconto_va - desconto_vt

        print("\n==== Folha de pagamento ====")
        print(f"Nome do funcionário: {nome}")
        print(f"Salário bruto R$ {salario_bruto:.2f}")
        print(f"Desconto INSS R$ {desconto_inss:.2f}")
        print(f"Desconto VA R$ {desconto_va:.2f}")
        print(f"Desconto VT R$ {desconto_vt:.2f}")
        print(f"Salário líquido R$ {salario_liquido:.2f}")
        print("="*30)

        salvar_folha_em_arquivo(nome,salario_bruto,desconto_inss,desconto_va,desconto_vt,va,vt,salario_liquido)

        novo = input("\nDeseja cadastrar outro funcionário (S/N): ").lower()

        if novo != "s":
            print("Fim do programa.")
            break

if __name__ == "__main__":
    folha_pagamento()        