""" 06. Crie uma classe para representar uma pessoa, com os atributosprivados de 
nome, data de nascimento e altura. 

Crie os métodos públicos necessários para 
sets e gets 

e também um método para 
imprimir todos dados de uma pessoa. 

Crie um método para calcular a idade da pessoa.

A data de nascimento pode ser informada como uma String (no formato
05/10/1982, por exemplo) e, no cálculo da idade, considere apenas o
ano da data de nascimento informada. """
from datetime import datetime 

class Pessoa:
    def __init__(self, n, dn, a):
        self.nome = n
        self.dn = dn
        self.altura = a
# sets
    def set_nome(self, nome):
        self.nome = nome

    def set_dn(self, dn):
        self.dn = dn

    def set_altura(self, altura):
        self.altura = altura
# gets
    def get_nome(self):
        return self.nome

    def get_dn(self):
        return self.dn

    def get_altura(self):
        return self.altura
# print dados
    def get_dados(self):
        print(f'Nome: {self.nome}, Data de Nascimento: {self.dn}, Altura: {self.altura}')
# idade:
    def idade(self):
        
        ano = datetime.today().year
        ano_pessoa = int(self.dn[-4:])
        print(f'Idade: {ano - ano_pessoa}')

teste_pessoa = Pessoa('Adamastor', '01/01/1987', '1.70')

teste_pessoa.get_dados()

teste_pessoa.idade()