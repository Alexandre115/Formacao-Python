class SistemaCobranca:
    def __init__(self, prestacao, dias_atraso, taxa_mensal):
        self.prestacao = prestacao
        self.dias_atraso = dias_atraso
        self.taxa_mensal = taxa_mensal

    def calcular_taxa_mensal(self):
        return (self.taxa_mensal / 100) / 30

    def calcular_valor_juros(self):
        taxa_diaria = self.calcular_taxa_mensal()
        juros = self.prestacao * taxa_diaria * self.dias_atraso
        return juros

    def calcular_valor_total(self):
        return self.prestacao + self.calcular_valor_juros()

if __name__ == "__main__":
    print("## Sistema de cobrança Tabajara ##")
    prestacao = float(input("Digite o valor da prestação R$ "))
    dias_atraso = int(input("Digite quantos dias a prestação está em atraso: "))
    taxa_mensal = int(input("Digite a taxa de juros mensal % "))

    cobranca = SistemaCobranca(prestacao, dias_atraso, taxa_mensal)

    juros = cobranca.calcular_valor_juros()
    total = cobranca.calcular_valor_total()

    print("#"*30)
    print(f"Valor da prestação R$ {prestacao:.2f}")
    print(f"Dias em atraso: {dias_atraso}")
    print(f"Taxa de juros cobrado % {taxa_mensal}")
    print(f"Valor do juros cobrado R$ {juros:.2f}")
    print(f"Valor final da prestação R$ {total:.2f}")        
        