def registrar_pedido():
    '''
    Função para mostrar o menu, pedir a escolha do usuário, 
    realizar o cálculo e o valor do desconto, se houver
    '''
    print("1 - Hambúrguer R$ 20,00")
    print("2 - Batata frita R$ 10,00")
    print("3 - Refrigerante R$ 8,00")
    print("4 - Suco natural R$ 12,00")
    print("5 - Sobremesa R$ 15,00")

    opcao = int(input("Escolha o produto (1 a 5): "))
    quantidade = int(input("Digite a quantidade: "))

    if opcao == 1:
        produto = "Hambúrguer"
        preco = 20
    elif opcao == 2:
        produto = "Batata frita"
        preco = 10
    elif opcao == 3:
        produto = "Refrigerante"
        preco = 8
    elif opcao == 4:
        produto = "Suco natural"
        preco = 12
    elif opcao == 5:
        produto = "Sobremesa"
        preco = 15
    else:
        print("Opção inválida!")

    total = preco * quantidade

    # Aplicar o desconto
    if total > 50:
        total_final = total * 0.9   
        desconto = total - total_final
        # total_final = total -(total * 0.1) 
    else:
        total_final = total

    desconto = total - total_final    

    # Exibir os resultados
    print("#"*30)
    print(f"Produto: {produto}")
    print(f"Quantidade {quantidade}")
    print(f"Valor total R$ {total:.2f}")
    print(f"Valor final R$ {total_final:.2f}")
    print(f"Valor do desconto R$ {desconto:.2f}")
    print("="*30)    

