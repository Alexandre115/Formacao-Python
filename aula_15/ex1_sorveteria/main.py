from compra import realizar_compra
from pagamento import aplicar_pagamento

def main():
    '''Função principal do programa'''
    total, quantidade_total = realizar_compra()
    print("#"*30)
    print(f"Quantidade total de picolés comprados: {quantidade_total} unidade(s)")
    total_final = aplicar_pagamento(total)
    print(f"Valor total da compra R$ {total_final:.2f}")
    print(f"## Obrigado por comprar na nossa sorveteria ##")

if __name__ == "__main__":
    main()    