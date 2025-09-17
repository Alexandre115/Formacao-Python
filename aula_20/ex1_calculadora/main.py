from calculadora import Calculadora

def main():
    print("## Calculadora em Python ##")
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    print("## Menu de operação matemáticas ##")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    opcao = int(input("Digite uma das opções: "))

    # Criar uma instância com a classe Calculadora e enviar os dados
    calc = Calculadora(n1, n2, opcao)
    resultado = calc.calcular()

    if resultado is None:
        if opcao == 4 and n2 == 0:
            print("Erro: Divisão por zero não é permitida!")
        else:
            print("Você escolheu uma operação matemática que não tem no sistema")
            print("Tente novamente!")

    else:
        print(f"Resultado da operação matemática: {resultado:.1f}")

if __name__ == "__main__":
    main()                 