def obter_dados_corretor():
    '''
    Solicitar o nome do corretor e o valor do imóvel
    '''
    print("## Corretora de imóveis TabajaraCorp ##")
    nome = input("Digite o nome do corretor de imóveis: ")

    while True:
        try:
            venda = float(input("Digite o valor do imóvel R$ "))
            if venda < 0:
                print("O valor do imóvel não pode ser negativo!")
            else:
                break
        except ValueError:
            print("Entrada inválida! Falha na Matrix.")

    return nome, venda    
def calcular_comissao(valor_venda):
    if valor_venda >= 100000:
        return valor_venda * 0.20
    elif valor_venda >= 70000:
        return valor_venda * 0.15
    else:
        return valor_venda * 0.10

def exibir_resultado(nome, comissao):
    print("#"*30) 
    print("## Informações do corretor ##")
    print(f"Nome do corretor: {nome}")
    print(f"Valor total da comissão da venda R$ {comissao:.2f}")
    print("#"*30)  

def main():
    '''
    Função principal para controlar o fluxo do programa
    '''      
    while True:
        nome, valor_venda = obter_dados_corretor()
        comissao = calcular_comissao(valor_venda)
        exibir_resultado(nome, comissao)

        continuar = input("Deseja continuar pesquisando: (s/n): ").lower()
        if continuar != 's':
            print("Programa finalizado!")
            break

if __name__ == "__main__":
    main()        


