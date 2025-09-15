'''
Criar uma lista vazia que vai armazenar os 5 números 
digitados pelo usuário
'''
num = []
#Lista de ordinais para exibir mensagens personalizadas
ordinais = ["primeiro","segundo","terceiro","quarto","quinto"]

#Loop para ler os 5 números do usuário
for i in range(5):
    #slocitar o número ao usuário
    valor = int(input(f"Digite o {ordinais[i]} número: "))
    num.append(valor)

print("#"*30)
for i in range(5):
    print(f"{ordinais[i].capitalize()} número digitado: {num[i]}")    