'''
Sistema para uma loja de brinquedos
'''
import os
from datetime import datetime

def exibir_menu_produto():
    print("## Menu de produtos ##")
    print("1 - Carrinho de controle remoto Super Máquina R$ 500,00")
    print("2 - Boneca Barbie R$ 300,00")
    print("3 - Boneco Cobra comandos em ação R$ 300,00")
    print("4 - Boneco fofão R$ 480,00")
    print("5 - Video game Atari R$ 820,00")
    print("6 - Jogo Super Mario R$ 100,00")
    print("7 - Bicicleta Caloi cross extra R$ 5.000,00")

def obter_preco_nome(produto_numero):
    produto = {
        1: (500, "Carrinho de controle remoto Super Máquina"),
        2: (300, "Boneca Barbie"),
        3: (300, "Boneco Cobra comandos em ação"),
        4: (480, "Boneco Fofão"),
        5: (820, "Video game Atari"),
        6: (100, "Jogo Super Mario"),
        7: (5000, "Caloi Cross Extra"),
    }    
    return produto.get(produto_numero, (0, "Produto inválido"))

def selecionar_produto():
    exibir_menu_produto()
    while True:
        try:
            numero = int(input("Digite o número do produto (1 a 7): "))
            if 1 <= numero <= 7:
                return numero
            else:
                print("Opção inválida! Digite novamente.")
        except ValueError:
            print("Entrada inválida! Digite um número.")

def selecionar_quantidade():
    while True:
        try:
            qtd = int(input("Digite a quantidade desejada: "))
            if qtd > 0:
                return qtd
            else:
                print("A quantidade deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

def adicionar_produtos(carrinho, subtotal):
    numero = selecionar_produto()
    preco, nome = obter_preco_nome(numero)
    quantidade = selecionar_quantidade()

    if numero in carrinho:
        carrinho[numero]["quantidade"] += quantidade
        carrinho[numero]["total"] += preco * quantidade
    else:
        carrinho[numero] = {
            "nome": nome,
            "preco_unitario": preco,
            "quantidade": quantidade,
            "total": preco * quantidade
        }  
    subtotal += preco * quantidade
    print(f"Subtotal atualizado R$ {subtotal:.2f}")
    return subtotal

def exibir_opcoes_pagamento():
    print("## Menu de opções de forma de pagamento ##")
    print("1 - A vista em dinheiro ou PIX - 5% de desconto")
    print("2 - No cartão de débito - mesmo valor")
    print("3 - Cartão de crédito em 1x - acréscimo de 5%")
    print("4 - Cartão de crédito em 2x - acréscimo de 6%")
    print("5 - Cartão de crédito em 3x - acréscimo de 7%")
    print("6 - Cartão de crédito em 4x - acréscimo de 8%")
    print("7 - Cartão de crédito em 5x - acréscimo de 10%")

def escolher_pagamento():
    exibir_opcoes_pagamento()
    while True:
        try:
            op = int(input("Digite a opção desejada: "))
            if 1 <= op <= 7:
                return op
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")   

def calcular_pagamento(subtotal, opcao):
    if opcao == 1:
        total = subtotal * 0.95
        parcelas = 1
        mensagem = "À vista em dinheiro/PIX - 5% desconto"
    elif opcao == 2:
        total = subtotal 
        parcelas = 1
        mensagem = "Cartão de débito - mesmo valor"
    elif opcao == 3:
        total = subtotal * 1.05
        parcelas = 1
        mensagem = "Cartão de crédito 1x - acréscimo 5%"
    elif opcao == 4:
        total = subtotal * 1.06
        parcelas = 2
        mensagem = "Cartão de crédito 2x - acréscimo 6%"
    elif opcao == 5:
        total = subtotal * 1.07
        parcelas = 3
        mensagem = "Cartão de crédito 3x - acréscimo 7%"
    elif opcao == 6:
        total = subtotal * 1.08
        parcelas = 4
        mensagem = "Cartão de crédito 4x - acréscimo 8%"
    elif opcao == 7:
        total = subtotal * 1.10
        parcelas = 5
        mensagem = "Cartão de crédito 5x - acréscimo 10%"
    else:
        total = subtotal
        parcelas = 1
        mensagem = "Forma de pagamento inválida!"

    valor_parcelas = total / parcelas
    return total, valor_parcelas, mensagem   

def exibir_resumo(carrinho, subtotal, total, parcela, texto_pagamento):
    print("="*30)
    print("Resumo da compra:")
    total_itens = 0
    for idx, (codigo, item) in enumerate(carrinho.items(), start=1):
        print(f"{idx}: {item['nome']} | Qtd: {item['quantidade']} | "
              f"Unitário: R$ {item['preco_unitario']:.2f} | "
              f"Total: R$ {item['total']:.2f}")
        total_itens += item['quantidade']
    print(f"Total de produtos comprados: {total_itens}")
    print(f"Subtotal da compra R$ {subtotal:.2f}")
    print(f"Valor da parcela R$ {parcela:.2f}")
    print(f"Total final R$ {total:.2f}")
    print(f"Forma de pagamento: {texto_pagamento}")
    print("="*30)

def gerar_relatorio(carrinho, subtotal, total, parcela, forma_pagamento):
    '''
    Gera um arquivo TXT com o resumo da compra e abre automaticamente
    '''
    nome = input("Digite o nome do arquivo para salvar: ")
    data_atual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = nome + f"_{data_atual}.txt"

    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write("### Relatório de compras - Loja de Brinquedos TBJC ###\n")
        f.write(f"Data e hora: {data_atual}\n\n")
        f.write("Itens comprados:\n")
        total_itens = 0
        for item in carrinho.values():
            f.write(f"- {item['quantidade']}x {item['nome']} "
                    f" | Unit: R$ {item['preco_unitario']:.2f} "
                    f" | Subtotal: R$ {item['total']:.2f}\n")
            total_itens += item['quantidade']
        f.write(f"\nTotal de produtos: {total_itens}\n")
        f.write(f"Subtotal: R$ {subtotal:.2f}\n")
        f.write(f"Forma de pagamento: {forma_pagamento}\n")
        f.write(f"Valor da parcela: R$ {parcela:.2f}\n")
        f.write(f"Total final: R$ {total:.2f}\n")
        f.write("\nObrigado por comprar conosco!\n")

    # Tentar abrir o arquivo automaticamente
    try:
        os.startfile(nome_arquivo)  # Windows
    except AttributeError:
        import subprocess
        try:
            subprocess.call(['open', nome_arquivo])   # macOS
        except:
            subprocess.call(['xdg-open', nome_arquivo])  # Linux

def main():
    print("## Loja de brinquedos TBJC ##")
    subtotal = 0.0
    carrinho = {}

    while True:
        subtotal = adicionar_produtos(carrinho, subtotal)
        continuar = input("Deseja adicionar mais um produto (S/N): ").lower()
        if continuar != 's':
            break

    print(f"Subtotal final da compra R$ {subtotal:.2f}")
    opcao_pagamento = escolher_pagamento()
    total, parcela, text_pagamento = calcular_pagamento(subtotal, opcao_pagamento)
    exibir_resumo(carrinho, subtotal, total, parcela, text_pagamento)

    # Chamar função para salvar e abrir o relatório
    gerar_relatorio(carrinho, subtotal, total, parcela, text_pagamento)

if __name__ == "__main__":
    main()
