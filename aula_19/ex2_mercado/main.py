from trakinas import VendaTrakinas

def main():
    # Apresentação inicial do sistema
    print("## Mercadinho Tabajara ##")
    print("Seja bem-vindo!")
    print("Preço da trakinas R$ 4,50 a unidade")
    print("Comprando mais de 10 unidades, você vai pagar R$ 4,00 a unidade")

    # Solicita a quantidade de trakinas para compra
    quantidade = int(input("Informe a quantidade de trakinas que deseja comprar: "))

    # Cria um objeto VendaTrakinas com a quantidade informada
    venda = VendaTrakinas(quantidade)

    # Calcula o valor total da compra e obtém o preço unitário aplicado
    valor_total = venda.calcular_valor_total()
    preco_unitario = venda.informar_preco_unitario()

    # Exibe os resultados para o usuário
    print("################################")
    print(f"Quantidade de trakinas que você comprou: {quantidade}")
    print(f"Você vai pagar R$ {preco_unitario:.2f} a unidade")
    print(f"Valor total da sua compra R$ {valor_total:.2f}")

if __name__ == "__main__":
    main()
