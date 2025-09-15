# Inicialização da lista de idades
idade = [] #vetor para armazenar 8 idades
soma = 0 # variável para acumular a soma das idades
maior = 0 # variável que vai guardar a maior idade
c = 0 # contador

# Entrada de dados: leitura das 8 idades
for c in range(1, 9): #De 1 até 8
    valor = int(input(f"Digite a idade da {c}ª pessoa: "))
    idade.append(valor) # adicionando a idade no vetor
    soma += valor

# Verificação das pessoas com mais de 25 anos
for c in range(8): # Os indices do vetor sao de 0 a 7
    if idade[c] > 25:
        print(f"Pessoa com mais de 25 anos na posição {c + 1}")  

# Encontrar a maior idade entre os dados informados
for c in range(8):
    if idade[c] > maior:
        maior = idade[c] # Vai atualizar a variável maior, toda vez uma idade for maior          

print(f"A maior idade digitada foi: {maior}")

media = soma / 8
print(f"Média das idades digitadas: {media:.2f}")