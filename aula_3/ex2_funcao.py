# Função para calcular a média das notas com função
def media(nota1, nota2, nota3, nota4):
    # Calcular a média das quatro notas
    resultado = (nota1+nota2+nota3+nota4) / 4
    return resultado
def main():
    print("## Sistema de notas utilizando função ##")
    n1 = int(input("Digite a primeira nota: "))
    n2 = int(input("Digite a Segunda nota: "))
    n3 = int(input("Digite a terceira nota: "))
    n4 = int(input("Digite a quarta nota: "))

    resultado = media(n1,n2,n3,n4)
    print(f"Média das notas digitadas: {resultado}")

if __name__ == "__main__":
    main()    