'''
Vamos criar uma lista com 5 posições, todas iniciadas 
com o valor 0
'''
num = [0] * 5
#Lista que simula o vetor[1..5]
# Solicitar que o usuário digite 5 números inteiros
num[0] = int(input("Digite o primeiro número: "))
num[1] = int(input("Digite o segundo número: "))
num[2] = int(input("Digite o terceiro número: "))
num[3] = int(input("Digite o quarto número: "))
num[4] = int(input("Digite o quinto número: "))

print("#"*30)
print("Primeiro número digitado: ",num[0])
print("Segundo número digitado: ",num[1])
print("Terceiro número digitado: ",num[2])
print("Quarto número digitado: ",num[3])
print("Quinto número digitado: ",num[4])