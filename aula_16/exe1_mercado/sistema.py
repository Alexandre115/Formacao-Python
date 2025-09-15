from menu import exibir_menu_produtos, exibir_forma_pagamento
from calculos import calcular_subtotal, calcular_pagamento

def sistema_caixa():
    '''Função para gerenciar o fluxo de venda no caixa do mercado'''
    total_arrecadado_dia = 0.0
    total_itens_vendidos = 0
    novo_cliente = 's'

    while novo_cliente.lower() == "s":
        total = 0.0
        quant_total = 0
        sn = "s"
        print("==== Mercadinho da tia Clotilde ====")

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

            print("="*30)
            print(f"Você adicionou {quantidade} unidade(s) de {produto}")
            print(f"Subtotal desta compra R$ {subtotal:.2f}")
            print(f"Valor total da compra até o momento R$ {total:.2f}")

            sn = input("Deseja adicionar mais produtos ao carrinho (S/N): ")

        print("="*30)
        print(f"Quantidade total de itens no carrinho: {quant_total} unidade(s)")
        print(f"Valor total da sua compra R$ {total:.2f}")
        print("="*30)
        exibir_forma_pagamento()   

        while True:
            try:
                pag = int(input("Escolha uma das opções (1 a 6): "))
                valor_pago, forma_pagamento = calcular_pagamento(total, pag)
                if valor_pago is None:
                    print("Você digitou uma forma de pagamento inválida!")
                    continue
                break
            except ValueError:
                print("Entrada inválida! Digite um número de 1 a 6")

        total_arrecadado_dia += valor_pago

        print("="*30)
        print("== Informações sobre a compra ==")
        print(f"Forma de pagamento: {forma_pagamento}")
        print(f"Quantidade total de produtos comprados: {quant_total} unidade(s)")
        print(f"Valor total da sua compra R$ {valor_pago:.2f}")

        novo_cliente = input("Deseja atender um novo cliente (S/N): ")

    print("="*30)
    print("#### Fechamento do dia ####")
    print(f"Total de itens vendidos no dia: {total_itens_vendidos} unidade(s)")
    print(f"Valor total arrecadado no dia R$ {total_arrecadado_dia:.2f}")                

