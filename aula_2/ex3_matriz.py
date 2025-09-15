# Objetivo: Ler uma matriz de tamanho definido pelo usuário
# Solicitando para o usuário o número de linhas e colunas para matriz
linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))

# Criar a matriz com o tamanho definido pelo usuário
matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]

# Variáveis auxiliares
soma_total = 0
maior_valor = None # Será definido no primeiro elemento lido
valores_pares = [] # Lista para armazenar os números pares

# Leitura da matriz e processamento de dados
for i in range(linhas):
    for j in range(colunas):
        valor = int(input(f"Digite um número para a posição [{i+1}, {j+1}]: "))
        matriz[i][j] = valor
        soma_total += valor

        # Verifica e armazena se o número é par
        if valor % 2 == 0:
            valores_pares.append(valor)

        # Define o maior valor (na primeira interação) ou atualizaq se necessário    
        if maior_valor is None or valor > maior_valor:
            maior_valor = valor

# Calcular a média dos valores da matriz
total_elemento = linhas * colunas
media = soma_total / total_elemento

print("\nMatriz formatada: ")
for linha in matriz:
    for item in linha:
        print(f"{item:4}", end=' ') # Imprime com alinhamento
    print() 

# Resultados finais
print("\nResultado final da análise")
print(f"Soma total dos elementos: {soma_total}")
print(f"Média dos valores: {media:.2f}")
print(f"Maior valor encontrado: {maior_valor}")
print(f"Números pares encontrados: {valores_pares}")       