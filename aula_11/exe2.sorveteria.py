import os
from datetime import datetime

def exibir_menu_picoles():
    print("## Sorveteria do sor Miguel ##")
    print("-- Menu de sabores --")
    print("1 - Picolé de uva R$ 1,00")
    print("2 - Picolé de laranja R$ 1,25")
    print("3 - Picolé de milho R$ 1,50")
    print("4 - Picolé de coco queimado R$ 1,80")
    print("5 - Picolé de tamarindo R$ 2,00")

def obter_preco_sabor(opcao):
    sabores = {
        1: ("Uva", 1.00),
        2: ("Laranja", 1.25),
        3: ("Milho", 1.50),
        4: ("Coco queimado", 1.80),
        5: ("Tamarindo", 2.00)
    }   
    return sabores.get(opcao, (None, 0))

def realizar_compra():
    total = 0.0
    quantidade_total = 0
    continuar = "s"
    lista_compras = []

    while continuar.lower() == "s":
        exibir_menu_picoles()
        try:
            opcao = int(input("Selecione uma das opções (1 a 5): ")) 
            nome_picole, preco = obter_preco_sabor(opcao)

            if nome_picole is None:
                print("Opção inválida! Tente novamente.")
                continue

            quantidade = int(input("Quantos picolés deseja comprar: "))
            subtotal = preco * quantidade
            total += subtotal
            quantidade_total += quantidade
            lista_compras.append((nome_picole, quantidade, subtotal))

            print("="*30)
            print(f"Você comprou {quantidade} unidade(s) do picolé de {nome_picole}")
            print(f"Subtotal da compra R$ {subtotal:.2f}")
            print(f"Total geral da compra R$ {total:.2f}")
        except ValueError:
            print("Entrada inválida! Digite um número válido.")
            continue

        continuar = input("Deseja continuar comprando (S/N): ")

    return total, quantidade_total, lista_compras

def exibir_menu_pagamento():
    print("#"*30)
    print("1 - A vista em dinheiro ou PIX - 10% de desconto")
    print("2 - Cartão de débito - 5% de desconto")
    print("3 - Cartão de crédito 1x - sem alteração no valor")
    print("4 - Cartão de crédito 2x - acréscimo de 5%")
    print("5 - Cartão de crédito 3x - acréscimo de 10%")
    print("6 - Cartão de crédito 4x - acréscimo de 15%")

def aplicar_pagamento(total):
    forma_pagamento = ""
    while True:
        try:
            exibir_menu_pagamento()
            opcao = int(input("Escolha uma opção de pagamento (1 a 6): "))

            if opcao == 1:
                desconto = total * 0.10
                total -= desconto
                forma_pagamento = "A vista em dinheiro ou PIX - 10% de desconto"   
                print(f"Valor do desconto R$ {desconto:.2f}")
            elif opcao == 2:
                desconto = total * 0.05
                total -= desconto
                forma_pagamento = "Cartão de débito - 5% de desconto"   
                print(f"Valor do desconto R$ {desconto:.2f}") 
            elif opcao == 3:
                forma_pagamento = "Cartão de crédito 1x - sem alteração no valor"  
                print("Valor da compra sem desconto ou acréscimo")
            elif opcao == 4:
                acrescimo = total * 0.05
                total += acrescimo
                forma_pagamento = "Cartão de crédito 2x - acréscimo de 5%" 
                print(f"Valor do acréscimo R$ {acrescimo:.2f}")
                print(f"Parcelado em 2x de R$ {total / 2:.2f}")
            elif opcao == 5:
                acrescimo = total * 0.10
                total += acrescimo
                forma_pagamento = "Cartão de crédito 3x - acréscimo de 10%" 
                print(f"Valor do acréscimo R$ {acrescimo:.2f}")
                print(f"Parcelado em 3x de R$ {total / 3:.2f}")
            elif opcao == 6:
                acrescimo = total * 0.15
                total += acrescimo
                forma_pagamento = "Cartão de crédito 4x - acréscimo de 15%" 
                print(f"Valor do acréscimo R$ {acrescimo:.2f}")
                print(f"Parcelado em 4x de R$ {total / 4:.2f}")
            else:
                print("Opção inválida! Tente novamente.")
                continue

            break
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

    return total, forma_pagamento   
def gerar_relatorio(lista_compras, total_final, quantidade_total, forma_pagamento):
    '''
    Função para gerar um arquivo .txt com o resumo da compra e vai abrir 
    o arquivo automaticamente
    '''     
    n_arquivo = input("Digite o nome do arquivo para salvar: ")
    data_atual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = n_arquivo + f" {data_atual}.txt"

    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write("### Relatório de compras - Sorveteria do Sor Miguel ###")
        f.write(f"Data e hora: {data_atual}\n\n")
        f.write("Itens comprados:\n")
        for nome, qtd, subt in lista_compras:
            f.write(f"- {qtd}x {nome} | Subtotal: R$ {subt:.2f}\n")
        f.write(f"\nTotal de picolés comprados: {quantidade_total} unidades\n")
        f.write(f"Forma de pagamento: {forma_pagamento}\n")
        f.write(f"Valor final da compra R$ {total_final:.2f}\n")
        f.write(f"\nObrigado por comprar no nosso mercado!\n")


    try:
        # Abrir o arquivo automaticamente (windows)
        os.startfile(nome_arquivo)
    except AttributeError:
        # Caso não seja Windows, tenta abrir de forma genérica
        import subprocess
        subprocess.call(['open', nome_arquivo]) # macOS
        # no Linux seria:
        # subprocess.call(['xdg-open', nome_arquivo])

def main():
    total, quantidade_total, lista_compras = realizar_compra()
    print(f"\nQuantidade total de picolés comprados: {quantidade_total} unidades")
    total_final, forma_pagamento = aplicar_pagamento(total)
    print(f"Valor total da compra R$ {total_final:.2f}")
    gerar_relatorio(lista_compras, total_final, quantidade_total, forma_pagamento)
    print("-- Relatório gerado e aberto automaticamente --")
    print("-- Obrigado por comprar no nossa sorveteria --")

if __name__ == "__main__":
    main()                        

