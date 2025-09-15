'''
DESAFIO

CRIE UM SISTEMA PARA UMA LOJA DE BRINQUEDOS ANTIGOS.
O SISTEMA DEVE:

Mostrar um menu de opções com pelo menos 7 brinquedos antigos e seus preços (ex.: Comandos em Ação, Fofão, Super Máquina, He-Man, Barbie, Autorama e Ferrorama).

Solicitar ao usuário que escolha um dos brinquedos (informando o número da opção).

Perguntar a quantidade desejada.

Calcular o valor total da compra.

Aplicar um desconto de 10% automaticamente se o valor total ultrapassar R$ 100,00.

Exibir ao final a mensagem com:

O nome do brinquedo escolhido.

A quantidade comprada.

O valor do desconto (se houver).

O valor total da compra.
'''
def menu_opcao():
    print("## Loja de Brinquedos Antigos TabajaCorp ##")
    print("-- Brinquedos disponíveis para venda --")
    print("1 - Comandos em Ação - R$ 40,00")
    print("2 - Fofão - R$ 60,00")
    print("3 - Super Máquina (Carrinho) - R$ 75,00")
    print("4 - He-Man (Boneco) - R$ 50,00")
    print("5 - Barbie Clássica - R$ 70,00")
    print("6 - Autorama - R$ 150,00")
    print("7 - Ferrorama - R$ 200,00")
    
    opcao = int(input("Selecione uma das opções (1 a 7): "))
    quantidade = int(input("Informe a quantidade que deseja comprar: "))
    return opcao, quantidade

def opcao_escolha(opcao, quantidade):
    if opcao == 1:
        total = quantidade * 40
        item = "Comandos em Ação"
    elif opcao == 2:
        total = quantidade * 60
        item = "Fofão"
    elif opcao == 3:
        total = quantidade * 75
        item = "Super Máquina"
    elif opcao == 4:
        total = quantidade * 50
        item = "He-Man"
    elif opcao == 5:
        total = quantidade * 70
        item = "Barbie Clássica"
    elif opcao == 6:
        total = quantidade * 150
        item = "Autorama"
    elif opcao == 7:
        total = quantidade * 200
        item = "Ferrorama"
    else:
        total = 0
        item = "Opção inválida"

    return total, item    

def aplicar_desconto(valor):
    """Aplica 10% de desconto se valor > 100"""
    if valor > 100:
        desconto = valor * 0.10
        valor_final = valor - desconto
        return valor_final, desconto
    return valor, 0

def main():
    print("#" * 45)
    opcao, quantidade = menu_opcao()
    total, item = opcao_escolha(opcao, quantidade)
    
    total_final, desconto = aplicar_desconto(total)

    print("\n===== RESUMO DA COMPRA =====")
    print(f"Item escolhido: {item}")
    print(f"Quantidade: {quantidade}")
    print(f"Valor bruto: R$ {total:.2f}")
    if desconto > 0:
        print(f"Desconto aplicado: -R$ {desconto:.2f} (10%)")
    print(f"TOTAL A PAGAR: R$ {total_final:.2f}")
    print("============================")

if __name__ == "__main__":
    main()
