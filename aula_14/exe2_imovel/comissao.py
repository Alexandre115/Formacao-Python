def obter_dados_corretor():
    '''
    Função que solicita o nome do corretor e o valor 
    do imóvel para venda
    '''
    print("## Imobiliaria Casa sen telha ##")
    nome = input("Digite o nome do corretor de imóveis: ")

    while True:
        try:
            venda = float(input("Digite o valor do imóvel R$ "))
            if venda < 0:
                print("O valor do imóvel não pode ser negativo.")
            else:
                break
        except ValueError:
            print("Entrada inválida!") 

    return nome, venda

def calcular_comissao(valor_venda):
    '''
    Função para calcular a comissão com base no valor do imóvel
    '''           
    if valor_venda >= 100000:
        return valor_venda * 0.20
    elif valor_venda >= 70000:
        return valor_venda * 0.15
    else:
        return valor_venda * 0.10
    
def exibir_resultado(nome, comissao):
    '''
    Função para exibir o nome do corretor e a 
    comissão da venda do imóvel
    '''
    print("== Informações do corretor ==")
    print(f"Nome do corretor: {nome}")
    print(f"Valor total da comissão da venda R$ {comissao:.2f}")
    print("="*30)

    