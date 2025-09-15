def menu_opcao():
    '''
    Sistema para uma sorveteria
    '''
    print("## Sorveteria TabajaCorp ##")
    print("-- Menu de sabores --")
    print("1 - Picolé de Uva R$ 1,00")
    print("2 - Picolé de Laranja R$ 1,25")
    print("3 - Picolé de Milho R$ 1,50")
    print("4 - Picolé de Coco queimado R$ 1,80")
    print("5 - Picolé de Tamarindo R$ 2,00")

    opcao = int(input("Selecione uma das opções (1 a 5): "))
    quantidade = int(input("Informe a quantidade de picolés que deseja comprar: "))

    return opcao, quantidade

def opcao_escolha(opcao, quantidade):
    if opcao == 1:
        total = quantidade * 1.00
        picole = "Uva"
    elif opcao == 2:
        total = quantidade * 1.25
        picole = "Laranja"
    elif opcao == 3:
        total = quantidade * 1.50
        picole = "Milho"
    elif opcao == 4:
        total = quantidade * 1.80
        picole = "Coco Queimado"
    elif opcao == 5:
        total = quantidade * 2.00
        picole = "Tamarindo"
    else:
        total = 0
        picole = "Opção inválida"

    return total, picole

def main():
    print("#" * 30)
    opcao, quantidade = menu_opcao()
    total, picole = opcao_escolha(opcao, quantidade)

    print(f"\nVocê escolheu {quantidade} picolé(s) de {picole}.")
    print(f"Valor total da compra: R$ {total:.2f}")
    
if __name__ == "__main__":
    main()
