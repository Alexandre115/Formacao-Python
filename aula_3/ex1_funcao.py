# Função para calcular o dobro de um número
def dobro(valor):
    # Variável local 'total' para armazenar o dobro de um valor
    total = valor * 2
    return total
def main():
    # Exibe uma mensagem que executa o programa
    print("## Sistema utilizando função ##")
    numero = float(input("Digite um número: "))
    resultado = dobro(numero)

    print(f"Valor do cálculo realizado na função: {resultado}")

if __name__ == "__main__":
    main()    