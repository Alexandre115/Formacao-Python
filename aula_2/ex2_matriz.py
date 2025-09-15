# Programa para ler uma matriz 3x3, e mostrar os valores
# Criando a matriz 3x3, inicializada com zeros
matriz = [[0 for _ in range(3)] for _ in range(3)]
# Variável para armazenar a soma total dos elementos
soma_total = 0
# Loop para preencher a matriz com os valores fornecidos pelo usuário
for i in range(3): # Linhas da matriz
    for j in range(3): # Colunas da matriz
        # Solicita ao usuário um número para posição [i][j]
        matriz[i][j] = int(input(f"Digite um número para a posição [{i+1}, {j+1}]: "))
        soma_total += matriz[i][j]

# Exibe a matriz formatada
print("\nMatriz 3x3: ")
for i in range(3):
    for j in range(3):
        # Imprimir o valor na mesma linha, separado por espaço
        print(matriz[i][j], end=' ')
    print() # Pula para a próxima linha, após imprimir uma linha na matriz            