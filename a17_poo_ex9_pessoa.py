'''
Crie uma classe chamada Pessoa. Ela deve ter 4 atributos: nome, idade, altura e peso. Também crie os métodos 
engordar, emagrecer, crescer e envelhecer.
OBS: Por padrão, a cada ano que a pessoa envelhece, ela deve crescer 0,5cm, desde que não tenha passado de 21 anos.
'''

class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def engordar(self, peso):
        if peso > 0:
            self.peso += peso
        
    def emagrecer(self, peso):
        if peso > 0:
            self.peso -= peso
        
    def crescer(self, centimetro):
        if centimetro > 0:
            self.altura += centimetro

    def envelhecer(self, anos):
        if anos > 0:
            self.idade += anos
        if self.idade < 21:
            self.crescer(0.05 * anos)

    def get_info(self):
        print(f'Infos da pessoa: nome: [ {self.nome} ], idade: [ {self.idade} ], altura: [ {self.altura} ], peso: [ {self.peso} ]')

pessoa_1 = Pessoa('ana', 10, 1.20, 20.00)

pessoa_1.get_info()

pessoa_1.envelhecer(10)

pessoa_1.get_info()

