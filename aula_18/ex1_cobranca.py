'''Sistema para calcular o valor de uma prestação com o juros por atraso'''
class SistemaCobranca:
    def __init__(self, valor_prestacao, dias_atraso, taxa_juros = 0.02):
        '''Método construtor da classe'''
        self.valor_prestacao =valor_prestacao
        self.dias_atraso = dias_atraso
        self.taxa_juros = taxa_juros

    def calcular_total(self):
        return self.valor_prestacao +(self.valor_prestacao * self.taxa_juros * self.dias_atraso)
    
    def calcular_juros(self):
        return self.calcular_total() - self.valor_prestacao
    
if __name__ == "__main__":
    print("## Sistema de cobrança Dindin ##")
    valor = float(input("Digite o valor da prestação R$ "))
    atraso = int(input("Digite quantos dias a prestação esta em atraso: "))

    # Instância da classe
    sistema = SistemaCobranca(valor, atraso)

    total = sistema.calcular_total()
    juros = sistema.calcular_juros() 

    print("#"*30)
    print(f"Valor da prestação R$ {valor:.2f}")
    print(f"Quantidade de dias em atraso: {atraso}")
    print(f"Valor do juros cobrado R$ {juros:.2f}")
    print(f"Valor total da prestação R$ {total:.2f}")   

        