from datetime import datetime

def salvar_folha_em_arquivo(nome,salario_bruto,desconto_inss,desconto_va,desconto_vt,va,vt,salario_liquido):
    data = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"folha_{nome.replace(' ', '_')}_{data}.txt"

    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write("==== Folha de pagamento ====\n")
        f.write(f"Nome do funcionário: {nome}\n")
        f.write(f"Salário bruto R$ {salario_bruto:.2f}\n")
        f.write(f"Desconto INSS R$ {desconto_inss:.2f}\n")
        f.write(f"Desconto VA (6%) R$ {desconto_va:.2f}\n")
        f.write(f"Desconto VT R$ {desconto_vt:.2f}\n")
        f.write(f"Vale alimentação recebido R$ {va:.2f}\n")
        f.write(f"Vale transporte recebido R$ {vt:.2f}\n")
        f.write(f"Salário líquido R$ {salario_liquido:.2f}\n")
        f.write("="*30)

    print(f"\n Folha de pagamento salva em: {nome_arquivo}")    