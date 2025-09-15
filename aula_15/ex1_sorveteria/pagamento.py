from menu import exibir_menu_pagamento

def aplicar_pagamento(total):
    '''Função para calcular o valor final com base na forma de pagamento 
    escolhido'''

    while True:
        try:
            exibir_menu_pagamento()
            opcao = int(input("Escolha uma opção de pagamento (1 a 6): "))

            if opcao == 1:
                desconto = total * 0.10
                total -= desconto
                print(f"Desconto de 10% aplicado R$ {desconto:.2f}")
            elif opcao == 2:
                desconto = total * 0.05
                total -= desconto
                print(f"Desconto de 5% aplicado R$ {desconto:.2f}")
            elif opcao == 3:
                print("Pagamento sem desconto ou acréscimo")
            elif opcao == 4:
                acrescimo = total * 0.05
                total += acrescimo
                print(f"Acréscimo de 5% aplicado R$ {acrescimo:.2f}")
                print(f"Parcelamento em 2x de R$ {total / 2:.2f}")
            elif opcao == 5:
                acrescimo = total * 0.10
                total += acrescimo
                print(f"Acréscimo de 10% aplicado R$ {acrescimo:.2f}")
                print(f"Parcelamento em 3x de R$ {total / 3:.2f}")
            elif opcao == 6:
                acrescimo = total * 0.15
                total += acrescimo
                print(f"Acréscimo de 15% aplicado R$ {acrescimo:.2f}")
                print(f"Parcelamento em 4x de R$ {total / 4:.2f}")
            else:
                print("Opção inválida! Digite um número válido")
                continue

            break
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

    return total        