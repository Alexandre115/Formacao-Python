'''Sistema para converter valores em reais para dolar e euro'''
class ConversorDeMoeda:
    def __init__(self):
        self.reais = 0.0
        self.cotacao_dolar = 0.0
        self.cotacao_euro = 0.0
        self.valor_dolar = 0.0
        self.valor_euro = 0.0

    def coletar_dados(self):
        print("## Agência de câmbio Tigrinho ##")
        self.cotacao_dolar = float(input("Informe a cotação do dolar hoje R$ "))
        self.cotacao_euro = float(input("Informe a cotação do euro hoje R$ ")) 
        self.reais = float(input("Informe o valor em reais para conversão R$ "))

    def calcular_conversao(self):
        self.valor_dolar = self.reais / self.cotacao_dolar
        self.valor_euro = self.reais / self.cotacao_euro

    def exibir_resultado(self):
        print("#"*30)
        print("## Resultado da conversão ##")
        print(f"Valor em reais R$ {self.reais:.2f}")
        print(f"Valor convertido para dolar $ {self.valor_dolar:.2f}")
        print(f"Valor convertido para euro € {self.valor_euro:.2f}")

if __name__ == "__main__":
    # Instância da classe
    conversor = ConversorDeMoeda()          
    conversor.coletar_dados()
    conversor.calcular_conversao()
    conversor.exibir_resultado()         