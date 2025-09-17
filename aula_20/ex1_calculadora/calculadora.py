class Calculadora:
    def __init__(self, numero1, numero2, opcao):
        self.numero1 = numero1
        self.numero2 = numero2
        self.opcao = opcao
        self.resultado = None

    def calcular(self):
        if self.opcao == 1:
            self.resultado = self.numero1 + self.numero2
        elif self.opcao == 2:
            self.resultado = self.numero1 - self.numero2
        elif self.opcao == 3:
            self.resultado = self.numero1 * self.numero2
        elif self.opcao == 4:
            if self.numero2 != 0:
                self.resultado = self.numero1 / self.numero2
            else:
                self.resultado = None
        else:
            self.resultado = None

        return self.resultado                
        