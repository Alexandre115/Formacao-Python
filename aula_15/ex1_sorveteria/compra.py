from menu import exibir_menu_picole

def obter_preco_sabor(opcao):
    '''Função para retornar o nome e o preço do picolé conforme a opção'''
    sabores = {
        1: ("Pistache", 1.00),
        2: ("Grozelia", 1.25),
        3: ("Morango", 1.50),
        4: ("7 Belo", 1.80),
        5: ("Creme de ovos", 2.00),
    }
    return sabores.get(opcao,(None, 0))

def realizar_compra():
    '''Função que permite realizar compras repetidas de picolés'''
    total = 0.0
    quantidade_total = 0
    continuar = "s"

    while continuar.lower() == "s":
        exibir_menu_picole()
        try:
            opcao = int(input("Selecione uma das opções (1 a 5): "))
            nome_picole, preco = obter_preco_sabor(opcao)

            if nome_picole is None:
                print("Opção inválida! Tente novamente.")
                continue

            quantidade = int(input("Digite a quantidade de picoles para compra: "))
            subtotal = preco * quantidade
            total += subtotal
            quantidade_total += quantidade

            print("="*30)
            print(f"Você comprou {quantidade} unidade(s) do picolé de {nome_picole}")
            print(f"Subtotal da compra R$ {subtotal:.2f}")
            print(f"Total da sua compra até o momento R$ {total:.2f}")
        except ValueError:
            print("Entrada inválida! Digite um número válido")
            continue

        continuar = input("Deseja continuar comprando (S/N): ")

    return total, quantidade_total        

