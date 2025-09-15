# Criando uma matriz 2x2
matriz = [[0,0],[0,0]]
# Preenchendo a matriz com valores do usuário
for i in range(2):#loop de 0 a 1
    for j in range(2):
        matriz[i][j] = int(input(f"Digite um número na posição [{i+1}, {j+1}]: "))

print("#"*30)
print(f"O valor que está na posição [1,1] é: {matriz[0][0]}")  
print(f"O valor que está na posição [1,2] é: {matriz[0][1]}") 
print(f"O valor que está na posição [2,1] é: {matriz[1][0]}")  
print(f"O valor que está na posição [2,2] é: {matriz[1][1]}")               