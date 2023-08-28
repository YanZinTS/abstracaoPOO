class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura


    def calcular_area(self):
        area = self.base * self.altura
        return area


medidasRetangulo = Retangulo(2, 4)

print('A área do retângulo é:', medidasRetangulo.calcular_area())