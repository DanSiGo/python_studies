""" 07. Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
Um veículo tem um certo consumo de combustivel (medidos em km / litro) e uma certa quantidade de combustivel no tanque.

O consumo é especificado no construtor e o nível de combustivel inicial é 0.

Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustivel no tanque de gasolina.
Esse método recebe como parâmetro a distância em km.

Forneça um método obterGasolina( ), que retorna o nível atual de combustivel.

Forneça um método adicionarGasolina( ), para abastecer o tanque.

Faça um programa para testar a classe Carro. Exemplo de uso:

meuFusca = Carro(15); # 15 quilômetros por litro de combustivel.

meuFusca.adicionarGasolina(20); # abastece com 20 litros de
combustivel.

meuFusca.andar(100); # anda 100 quilômetros.

meuFusca.obterGasolina() # Imprime o combustivel que resta no
tanque. """

import time

class Carro:
    ''' class para fazer um carro '''
    def __init__(self, consumo) -> None:
        self.consumo = consumo
        self.tanque = 0

    def andar(self, distancia):
        self.tanque -= distancia

    def obter_gasolina(self):
        return self.tanque / 15
    
    def adicionar_gasolina(self, gasolina):        
        self.tanque += (gasolina * self.consumo)

'''
meuFusca = Carro(15) # 15 quilômetros por litro de combustivel.
litros = float(input('Quantos litros de combustível quer adicionar? '))
meuFusca.adicionar_gasolina(litros) # abastece com 20 litros de combustivel.
print('--------------------')
print(f'Você adicionou {litros} de combustível')
print('--------------------')
print(f'O carro conta com {meuFusca.obter_gasolina()} litros de combustível')
print('--------------------')
andar = float(input('Informe a quantidade de km percorridos: '))
meuFusca.andar(andar); # anda 100 quilômetros.
print('--------------------')
print(f'O carro percorreu {andar}km')
print('--------------------')
print(f'O carro conta com {meuFusca.obter_gasolina():.2f} litros de combustível')
print('--------------------')
''' 
x = Carro(15)
print(x.__doc__)
