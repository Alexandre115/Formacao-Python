def calcular_subtotal(opcao, quantidade):
    '''Função para calcular o subtotal de uma compra com 
    base na opção e quantidade'''
    if opcao == 1:
        return quantidade *5, "Arroz 1Kg"
    elif opcao == 2:
        return quantidade * 7.5, "Feijão 1Kg"
    elif opcao == 3:
        return quantidade * 4, "Leite 1Lt"
    elif opcao == 4:
        return quantidade * 30, "Café 500Gr"
    else:
        return 0, "Opção inválida"
    
def calcular_pagamento(total, pag):
    '''Função para calcular o valor do pagamento de acordo 
    com a forma escolhida'''
    if pag == 1:
        return total * 0.90, "A vista em dinheiro ou PIX - 10% de desconto"
    elif pag == 2:
        return total * 0.95, "Cartão de débito - 5% de desconto"
    elif pag == 3:
        return total, "Cartão de crédito em 1x - mesmo valor"
    elif pag == 4:
        return total * 1.05, "Cartão de crédito em 2x - acréscimo de 5%"
    elif pag == 5:
        return total * 1.10, "Cartão de crédito em 3x - acréscimo de 10%"
    elif pag == 6:
        return total * 1.15, "Cartão de crédito em 4x - acréscimo de 15%"
    else:
        return None, "Opção inválida"

