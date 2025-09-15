from comissao import obter_dados_corretor, calcular_comissao, exibir_resultado

def main():
    while True:
        nome, valor_venda = obter_dados_corretor()
        comissao = calcular_comissao(valor_venda)
        exibir_resultado(nome, comissao)

        continuar = input("Deseja pesquisar para um novo corretor (S/N): ").lower()
        if continuar != 's':
            print("Sistema finalizado com sucesso.")
            break

if __name__ == "__main__":
    main()        

