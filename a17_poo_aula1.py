class Triangulo:
    # atributos
    lado_a = None
    lado_b = None
    lado_c = None

    # construtor
    def __init__(self, la, lb, lc):
        self.lado_a = la
        self.lado_b = lb
        self.lado_c = lc
    
    # métodos
    def calcular_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c
    
    def get_maior_lado(self):
        if self.lado_a > self.lado_b and self.lado_a > self.lado_c:
            return lado_a
        elif self.lado_b > self.lado_a and self.lado_b > self.lado_c:
            return self.lado_b
        else:
            return self.lado_c

la = float(input('Informe o lado A: '))
lb = float(input('Informe o lado B: '))
lc = float(input('Informe o lado C: '))

t1 = Triangulo(la, lb, lc)

print(f'O valor do lado A é: {t1.lado_a}')
print(f'O valor do lado B é: {t1.lado_b}')
print(f'O valor do lado C é: {t1.lado_c}')

print(f'O perímetro é: {t1.calcular_perimetro()}')
print(f'O maior lado é: {t1.get_maior_lado()}')