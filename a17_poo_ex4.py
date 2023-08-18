class Calculadora:
    numero_1 = None
    numero_2 = None

# construtor
    def __init__(self, n1, n2):
        self.numero_1 = n1
        self.numero_2 = n2
# get
    def get_valores(self):
        return f'Valor 1: [{self.numero_1}] e valor 2: [{self.numero_2}]'
# sets
    def set_numero1(self, novo_1):
        self.numero_1 = novo_1
    def set_numero2(self, novo_2):
        self.numero_2 = novo_2
# métodos
    def soma(self):
        return self.numero_1 + self.numero_2
    
    def subtracao(self):
        return self.numero_1 - self.numero_2

    def multiplicacao(self):
        return self.numero_1 * self.numero_2
        
    def divisao(self):
        return self.numero_1 / self.numero_2


n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))

calculo_1 = Calculadora(n1, n2)
print(calculo_1.get_valores())

print(f'''Esses são os calculos:\nsoma: {calculo_1.soma()}\nsubtração: {calculo_1.subtracao()}
multiplicação: {calculo_1.multiplicacao()}\ndivisão: {calculo_1.divisao()}''')

calculo_1.set_numero1(int(input('Informe novo primeiro valor: ')))
calculo_1.set_numero2(int(input('Informe novo segundo valor: ')))
print(calculo_1.get_valores())
print(f'''Esses são os calculos:\nsoma: {calculo_1.soma()}\nsubtração: {calculo_1.subtracao()}
multiplicação: {calculo_1.multiplicacao()}\ndivisão: {calculo_1.divisao()}''')