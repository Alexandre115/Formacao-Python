'''
DESAFIO

CRIE UM SISTEMA PARA UMA PIZZARIA.
O SISTEMA DEVE:

Mostrar um menu de opções com pelo menos 5 pizzas diferentes e seus preços.

Solicitar ao usuário que escolha uma das pizzas (informando o número da opção).

Perguntar a quantidade de pizzas desejada.

Calcular o valor total da compra.

Aplicar um desconto de 10% automaticamente se o valor total ultrapassar R$ 100,00.

Exibir ao final a mensagem:

O nome da pizza escolhida.

A quantidade.

O valor do desconto (se houver).

O valor total da compra.
'''
def menu_opcao():
    print("## Pizzaria TabajaraCorp ##")
    print("-- Menu de Sabores --")
    print("1 - Pizza de Marguerita R$ 40,00")
    print("2 - Pizza De Calabresa R$ 45,00")
    print("3 - Pizza de Frango R$ 50,00")
    print("4 - Pizza de Quatro queijos R$ 55,00")
    print("5 - Pizza de Pudin R$ 60,00")
    opcao = int(input("Selecione uma das opções (1 a 5): "))
    quantidade = int(input("Informe a quantidade de pizzas que deseja comprar: "))

    return opcao, quantidade
def opcao_escolha(opcao, quantidade):
    if opcao == 1:
        total = quantidade * 40.00
        pizza = "Marguerita"
    elif opcao == 2:
        total = quantidade * 45.00
        pizza = "Calabresa"
    elif opcao == 3:
        total = quantidade * 50.00
        pizza = "Frango"
    elif opcao == 4:
        total = quantidade * 55.00
        pizza = "Quatro queijos"
    elif opcao == 5:
        total = quantidade * 60.00
        pizza = "Pudin"
    else:
        total = 0
        pizza = "Opção inválida"

    # verificar o desconto
    if total > 100:
        desconto = total * 0.1
        total_com_desconto = total - desconto
        return total_com_desconto, pizza, desconto
    else:
        return total, pizza, 0

def main():
    print("#"*30)
    opcao, quantidade = menu_opcao()
    total, pizza, desconto = opcao_escolha(opcao, quantidade)   

    print(f"Vovê escolheu {quantidade} pizza de {pizza}")
    if desconto > 0:
        print(f"Desconto aplicado R$ {desconto:.2f}")
    print(f"Valor total da compra R$ {total:.2f}")

if __name__ == "__main__":
    main()    

