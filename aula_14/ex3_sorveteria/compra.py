def obter_opcao():
    '''
    Função para solicitar ao usuário uma opção de picolé válido
    '''
    while True:
        try:
            opcao = int(input("Selecione uma das opções (1 a 5): "))
            if 1 <= opcao <= 5:
                return opcao # Retorna se a opção for válida
            else: 
                print("Opção inválida! Escolha um número entre 1 e 5")
        except ValueError:
            print("Entrada inválida! Digite apenas números")

def obter_quantidade():
    '''
    Função para solicitar ao usuário uma quantidade válida 
    (maior que zero)
    '''             
    while True:
        try:
            quantidade = int(input("Digite a quantidade de picolés: "))
            if quantidade > 0:
                return quantidade
            else:
                print("A quantidade deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida! Digite apenas números")

def calcular_subtotal(opcao, quantidade):
    '''
    Função para calcular o subtotal da compra e retorna o 
    nome do sabor
    '''          
    # Dicionário com preços dos picolés
    preco = {1: 1.00, 2: 1.25, 3: 1.50, 4: 1.80, 5: 2.00}
    # Dicionário com os nomes dos sabores
    sabores = {
        1: "Leite condensado",
        2: "Limão Siciliano",
        3: "Manga",
        4: "Abacate",
        5: "Tangerina"
        }            
    preco_unitario = preco[opcao] # Buscar o preço conforme a opção
    subtotal = quantidade * preco_unitario
    sabor = sabores[opcao] # Buscar o nome do sabor
    return subtotal, sabor

def deseja_continuar():
    '''
    Função para perguntar ao usuário se deseja continuar comprando
    '''     
    while True:
        resposta = input("Deseja continuar comprando (S/N): ").lower()
        if resposta in ["s", "n"]:
            return resposta == "s" # Retorna True para "s" e False para "n"
        else:
            print("Resposta com 'S' para sim ou 'N' para não." )