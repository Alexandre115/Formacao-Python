'''
DESAFIO

CRIE UM SISTEMA PARA UMA LANCHONETE.
O SISTEMA DEVE:

Mostrar um menu de opções com pelo menos 5 lanches diferentes e seus preços.

Solicitar ao usuário que escolha um dos lanches (informando o número da opção).

Perguntar a quantidade de lanches desejada.

Calcular o valor total da compra.

Exibir ao final a mensagem:

O nome do lanche escolhido.

A quantidade.

O valor total da compra.

Dica: Use como referência o exemplo do código da sorveteria, mas adapte os 
nomes dos produtos e preços para lanches.
'''
def menu_opcao():
    #Menu de opções, escolha do produto e quantidade
    print("## Lanchonete TabajaCorp ##")
    print("1 - X Frango R$ 10,00")
    print("2 - X Salada R$ 10,50")
    print("3 - X Tudo R$ 12,00")
    print("4 - Cachorro quente R$ 10,00")
    print("5 - Torrada R$ 5,00")

    opcao = int(input("Selecione uma das opções (1 a 5): "))
    quantidade = int(input("Informe a quantidade de lanches que deseja comprar: "))

    return opcao, quantidade

def opcao_escolha(opcao, quantidade):
    if opcao == 1:
        total = quantidade * 10.00
        lanche = "X Frango"
    elif opcao == 2:
        total = quantidade * 10.50
        lanche = "X Salada"
    elif opcao == 3:
        total = quantidade * 12.00
        lanche = "X Tudo"
    elif opcao == 4:
        total = quantidade * 10.00
        lanche = "Cachorro quente"
    elif opcao == 5:
        total = quantidade * 5.00
        lanche = "Torrada"
    else:
        total = 0
        lanche = "Opção inválida"

    return total, lanche

def main():
    print("#"*30)   
    opcao, quantidade = menu_opcao()
    total, lanche = opcao_escolha(opcao, quantidade)
    print(f"Você escolheu {quantidade} lanche(s) de {lanche}")
    print(f"Valor total da compra R$ {total:.2f}") 

if __name__ == "__main__":
    main()    
