'''
Sistema para uma sorveteria.
O cliente pode realizar a compra de vários produtos e escolher o método de 
pagamento. O sistema permite registrar compras de vários clientes e,
ao final, exibe o fechamento do caixa.
'''
def exibir_menu_picoles():
    print("## Sorveteria TabajaraCorp ##")
    print("-- Menu de sabores --")
    print("1 - Picolé de Uva R$ 1,00")
    print("2 - Picolé de Laranja R$ 1,25")
    print("3 - Picolé de Milho R$ 1,50")
    print("4 - Picolé de Coco queimado R$ 1,80")
    print("5 - Picolé de Tamarindo R$ 2,00")

def obter_preco_sabor(opcao):
    '''
    Retornar o nome e o preço do picolé conforme a opção escolhida
    '''    
    sabores = {
        1: ("Uva", 1.00),
        2: ("Laranja", 1.25),
        3: ("Milho", 1.50),
        4: ("Coco queimado", 1.80),
        5: ("Tamarindo", 2.00),
    }
    return sabores.get(opcao, (None, 0))

def realizar_compra():
    """
    Função para realizar compras e o cliente escolher vários sabores
    """
    total = 0.0
    quantidade_total = 0
    continuar = 's'

    while continuar.lower() == "s":
        exibir_menu_picoles()

        try:
            opcao = int(input("Selecione uma das opções (1 a 5): "))
            nome_picole, preco = obter_preco_sabor(opcao)

            if nome_picole is None:
                print("Opção inválida! Tente novamente.")
                continue

            quantidade = int(input("Quantos picolés você deseja comprar? "))
            subtotal = preco * quantidade
            total += subtotal
            quantidade_total += quantidade

            print("#"*30)
            print(f"Você comprou {quantidade} unidade(s) do picolé de {nome_picole}")
            print(f"Subtotal da compra R$ {subtotal:.2f}")
            print(f"Total da compra até o momento R$ {total:.2f}")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
            continue

        continuar = input("Deseja continuar comprando (S/N): ")

    return total, quantidade_total

def exibir_menu_pagamento():
    '''
    Função para exibir as opções de forma de pagamento
    '''       
    print("#"*30)
    print("## Menu de forma de pagamento ##")
    print("1 - A vista em dinheiro ou PIX - 10% de desconto.")
    print("2 - Cartão de débito - 5% de desconto")
    print("3 - Cartão de crédito 1x - mesmo valor")
    print("4 - Cartão de crédito 2x - acréscimo de 5%")
    print("5 - Cartão de crédito 3x - acréscimo de 10%")
    print("6 - Cartão de crédito 4x - acréscimo de 15%")

def aplicar_pagamento(total):
    '''
    Função para calcular o valor final da compra, com base na forma de 
    pagamento escolhido
    '''    
    while True:
        try:
            exibir_menu_pagamento()
            opcao = int(input("Escolha uma opção de pagamento (1 a 6): "))

            if opcao == 1:
                desconto = total * 0.1
                total -= desconto
                print(f"Desconto de 10% aplicado -R$ {desconto:.2f}")
            elif opcao == 2:
                desconto = total * 0.05
                total -= desconto
                print(f"Desconto de 5% aplicado -R$ {desconto:.2f}")
            elif opcao == 3:
                print("Pagamento sem desconto ou acréscimo.")
            elif opcao == 4:
                acrescimo = total * 0.05
                total += acrescimo
                print(f"Acréscimo de 5% aplicado +R$ {acrescimo:.2f}")
                print(f"Parcelado em 2x de R$ {total / 2:.2f}")
            elif opcao == 5:
                acrescimo = total * 0.10
                total += acrescimo
                print(f"Acréscimo de 10% aplicado +R$ {acrescimo:.2f}")
                print(f"Parcelado em 3x de R$ {total / 3:.2f}")
            elif opcao == 6:
                acrescimo = total * 0.15
                total += acrescimo
                print(f"Acréscimo de 15% aplicado +R$ {acrescimo:.2f}")
                print(f"Parcelado em 4x de R$ {total / 4:.2f}")
            else:
                print("Opção de pagamento inválida. Tente novamente.")
                continue

            break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

    return total        

def main():
    # Variáveis para o caixa geral
    total_caixa = 0.0
    total_produtos = 0

    while True:
        total, quantidade_total = realizar_compra()
        print("-"*30)
        print(f"Quantidade total de picolés comprados: {quantidade_total} unidade(s)")
        total_final = aplicar_pagamento(total)
        print(f"Valor total da compra R$ {total_final:.2f}")

        # Atualizando o caixa geral
        total_caixa += total_final
        total_produtos += quantidade_total

        novo_cliente = input("\nDeseja realizar a compra para um novo cliente? (S/N): ")
        if novo_cliente.lower() != 's':
            break

    # Fechamento do caixa
    print("="*40)
    print("## FECHAMENTO DO CAIXA ##")
    print(f"Quantidade total de produtos vendidos: {total_produtos}")
    print(f"Valor total arrecadado: R$ {total_caixa:.2f}")
    print("="*40)

if __name__ == "__main__":
    main()
