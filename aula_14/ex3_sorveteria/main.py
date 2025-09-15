from menu import exibir_menu
from compra import obter_opcao, obter_quantidade, calcular_subtotal, deseja_continuar

def main():
    '''
    Função principal que processa toda compra
    '''
    total = 0.0
    quanttotal = 0
    continuar = True

    # Controle do loop principal
    while continuar:
        exibir_menu() # Exibe o meu de sabores
        opcao = obter_opcao() # Obtém a escolha do sabor
        quantidade = obter_quantidade() # Obtém a quantidade desejada
        subtotal, sabor = calcular_subtotal(opcao, quantidade)

        # Exibe detalhes da compra e a quantidade
        print("="*30)
        print(f"Você comprou {quantidade} unidade(s) do picolé de {sabor}")
        print(f"Subtotal R$ {subtotal:.2f}")

        # Atualizar o total geral e a quantidade geral
        total += subtotal
        quanttotal += quantidade

        print(f"Valor total da sua compra até o momento R$ {total:.2f}")
        print("="*30)

        # Verifica se o cliente deseja continuar
        continuar = deseja_continuar()

    # Exibe o resumo final da compra
    print("## Resumo final da compra ##")
    print(f"Quantidade total de picolés comprados: {quanttotal} unidade(s)")
    print(f"Valor total da sua compra R$ {total:.2f}")
    print(f"== Obrigado por comprar na nossa sorveteria ==")


if __name__ == "__main__":
    main()    

