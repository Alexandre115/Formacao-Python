# Função para calcular a soma dos elementos de uma lista
def calcular_soma(lista):
    # a função sum é nativa do pytho e soma todos os elementos de uma lista
    return sum(lista)

# Função para encontrar o maior valor em uma lista
def encontrar_maior(lista):
    # a função max retorna o maior valor de uma lista
    return max(lista)

# Função para encontrar o menor valor de uma lista
def encontrar_menor(lista):
    # A função min retorna o menor valor de uma lista
    return min(lista)

# função para calcular a média dos valores de uma lista
def calcular_media(lista):
    # a função len faz a média pelos elementos somados
    return sum(lista) / len(lista)

# função para contar os números pares da lista
def contar_pares(lista):
    return len([num for num in lista if num % 2 == 0])

# função principal que executa as operações
def main():
    # Solicitar ao usuário que insera 5 números inteiros
    lista = []
    for i in range(5):
        num = int(input(f"Digite o {i+1}ª número: "))
        lista.append(num)

    # Exibir os resultados de todas as operações nas funções
    print("#"*30)
    print(f"Soma dos números: {calcular_soma(lista)}")
    print(f"Maior número: {encontrar_maior(lista)}")
    print(f"Menor número: {encontrar_menor(lista)}")
    print(f"Média dos números: {calcular_media(lista):.2f}")
    print(f"Quantidade de números pares: {contar_pares(lista)}")

# Executar a função principal
if __name__ == "__main__":
    main()        