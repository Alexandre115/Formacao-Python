import os
from datetime import datetime

def exibir_menu_produtos():
    print("## Menu de Produtos ##")
    print("1 - Arroz R$ 5,00")
    print("2 - Feijão R$ 7,50")
    print("3 - Leite R$ 4,00")
    print("4 - Café R$ 30,00")

def calcular_subtotal(opcao, quantidade):
    if opcao == 1:
        return quantidade * 5.00, "Arroz 1Kg"
    elif opcao == 2:
        return quantidade * 7.50, "Feijão 1Kg"
    elif opcao == 3:
        return quantidade * 4.00, "Leite 1Lt"
    elif opcao == 4:
        return quantidade * 30.00, "Café 500Gr"
    else:
        return 0, "Opção inválida"
    
def exibir_forma_pagamento():
    print("## Forma de pagamento ##") 
    print("1 - A vista em dinheiro ou PIX - 10% de desconto")
    print("2 - Cartão de débito - 5% de desconto")
    print("3 - Cartão de crédito 1x - mesmo valor")
    print("4 - Cartão de crédito 2x - acréscimo de 5%")
    print("5 - Cartão de crédito 3x - acréscimo de 10%")
    print("6 - Cartão de crédito 4x - acréscimo de 15%")

def calcular_pagamento(total, pag):
    if pag == 1:
        return total - (total * 0.1), "À vista (dinheiro/PIX) - 10% desconto"
    elif pag == 2:
        return total * 0.95, "Cartão de débito - 5% desconto"
    elif pag == 3:
        return total, "Cartão de crédito 1x - mesmo valor"
    elif pag == 4:
        return total * 1.05, "Cartão de crédito 2x - acréscimo 5%"
    elif pag == 5:
        return total * 1.10, "Cartão de crédito 3x - acréscimo 10%"
    elif pag == 6:
        return total * 1.15, "Cartão de crédito 4x - acréscimo 15%"
    else:
        return None, "Opção inválida"

def salvar_nota_fiscal(itens, quant_total, valor_pago, forma_pagamento):
    '''
    Gera um arquivo TXT com a nota fiscal do cliente e abre automaticamente
    '''
    data_atual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"NotaFiscal_{data_atual}.txt"

    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write("### Mercadinho Tá Barato TBJ ###\n")
        f.write(f"Data e hora: {data_atual}\n\n")
        f.write("Itens comprados:\n")
        for item in itens:
            f.write(f"- {item['quantidade']}x {item['produto']} "
                    f"| Subtotal: R$ {item['subtotal']:.2f}\n")
        f.write("\n")
        f.write(f"Quantidade total de produtos: {quant_total}\n")
        f.write(f"Forma de pagamento: {forma_pagamento}\n")
        f.write(f"Valor total pago: R$ {valor_pago:.2f}\n")
        f.write("\nObrigado pela preferência!\n")

    # Abrir automaticamente conforme o sistema operacional
    try:
        os.startfile(nome_arquivo)  # Windows
    except AttributeError:
        import subprocess
        try:
            subprocess.call(['open', nome_arquivo])   # macOS
        except:
            subprocess.call(['xdg-open', nome_arquivo])  # Linux

def sistema_caixa():
    total_arrecadado_dia = 0.0
    total_itens_vendidos = 0

    novo_cliente = 's'
    # esse while controla o sistema geral
    while novo_cliente.lower() == "s":
        total = 0.0
        quant_total = 0
        itens = []  # lista para registrar os produtos do cliente
        sn = "s"
        print("## Mercadinho Ta barato TBJ ##")
        # esse while controla as compras do cliente
        while sn.lower() == "s":
            exibir_menu_produtos()
            try:
                opcao = int(input("Selecione uma das opções (1 a 4): "))
                if opcao not in [1, 2, 3, 4]:
                    print("Você escolheu uma opção inválida!")
                    continue
                quantidade = int(input("Quantos produtos deseja comprar: "))
            except ValueError:
                print("Entrada inválida! Digite apenas números.")
                continue  

            subtotal, produto = calcular_subtotal(opcao, quantidade) 
            total += subtotal
            quant_total += quantidade
            total_itens_vendidos += quantidade

            # registrar produto na lista para salvar depois
            itens.append({"produto": produto, "quantidade": quantidade, "subtotal": subtotal})

            print("="*30)
            print(f"Você adicionou {quantidade} unidade(s) de {produto}")
            print(f"Subtotal desta compra R$ {subtotal:.2f}")
            print(f"Valor total acumulado no carrinho R$ {total:.2f}")
            print("="*30)

            sn = input("Deseja adicionar mais produtos ao carrinho (S/N): ")

        print("="*30)
        print(f"Quantidade total de itens no carrinho: {quant_total} unidade(s)")
        print(f"Valor total da sua compra R$ {total:.2f}")
        exibir_forma_pagamento()

        while True:
            try:
                pag = int(input("Escolha uma opção de forma de pagamento (1 a 6): "))
                valor_pago, forma_pagamento = calcular_pagamento(total, pag)
                if valor_pago is None:
                    print("Você escolheu uma forma de pagamento inválida!")
                    continue
                break
            except ValueError:
                print("Entrada inválida! Digite um número de 1 a 6.")

        total_arrecadado_dia += valor_pago

        print("="*30)
        print("## Nota fiscal ##")
        print(f"Forma de pagamento: {forma_pagamento}")
        print(f"Quantidade total de produtos comprados: {quant_total} unidade(s)") 
        print(f"Valor total da sua compra R$ {valor_pago:.2f}")

        # salvar nota fiscal do cliente
        salvar_nota_fiscal(itens, quant_total, valor_pago, forma_pagamento)

        novo_cliente = input("Deseja atender um novo cliente: (S/N): ")

    print("="*30)
    print("## Fechamento do caixa ##")
    print(f"Total de itens vendidos no dia: {total_itens_vendidos} unidade(s)")
    print(f"Valor total arrecadado no dia R$ {total_arrecadado_dia:.2f}")

if __name__ == "__main__":
    sistema_caixa()
