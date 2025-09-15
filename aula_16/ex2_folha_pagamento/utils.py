def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

def ler_str(mensagem):
    return input(mensagem).strip()            