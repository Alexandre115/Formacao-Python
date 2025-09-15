'''
Sistema para venda de carros antigos
'''
def menu_opcao():
    print("## Loja de Clássicos antigos TabajaCorp ##")
    print("-- Veículos disponíveis para venda --")
    print("1 - Fusca 1975 - R$ 25.000,00")
    print("2 - Opala 1980 - R$ 45.000,00")
    print("3 - Maverick 1974 - R$ 70.000,00")
    print("4 - Chevette 1985 - R$ 20.000,00")
    print("5 - Dodge Changer 1973 - R$ 120.000,00")
    opcao = int(input("Selecione uma das opções (1 a 5): "))
    quantidade = int(input("Informe a quantidade de veículos que deseja comprar: "))

    return opcao, quantidade

def opcao_escolha(opca, quantida):
    if opca == 1:
        total = quantida * 25000
        carro = "Fusca 1975"
    elif opca == 2:
        total = quantida * 45000
        carro = "Opala 1980"
    elif opca == 3:
        total = quantida * 70000
        carro = "Maverick 1974"
    elif opca == 4:
        total = quantida * 20000
        carro = "Chevette 1985"
    elif opca == 5:
        total = quantida * 120000
        carro = "Dodge Changer 1973"
    else:
        total = 0
        carro = "Opção inválida"

    return total, carro    

def main():
    print("#"*30)
    op, quanti = menu_opcao()
    total, carro = opcao_escolha(op, quanti)

    print(f"Você escolheu a opção {op}")
    print(f"Você escolheu {quanti} carro(s)")
    print(f"Carro que você comprou foi: {carro}")
    print(f"Valor total da sua compra R$ {total:.2f}")

if __name__ == "__main__":
    main()    