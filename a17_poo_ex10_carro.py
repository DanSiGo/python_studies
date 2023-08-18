'''
Criar uma classe de Carro, que corre até no máximo 120km/h. O carro deve ser cadastrado com marca,
modelo, ano, velocidade, se está ligado ou não e se é automático ou não.
O carro deve conter funcionalidades de:
- ligar
- Acelerar: apenas se o carro estiver ligado (uma quantidade que não passe da velocidade máxima
de 120.
- desligar
- verificarMacha com as regras abaixo:
- 1a marcha: 0 a 20km
- 2a marcha: ao atingir 20 km/h;
- 3a marcha: entre 30 e 35 km/h;
- 4a marcha: entre 45 e 50 km/h; e.
- 5a marcha: acim de 60 km/h.
'''

class Carro:
    def __init__(self, marca, modelo, ano, velocidade, ligado, automatico):
        self.marca = marca
        self.modelo = modelo      
        self.ano = ano
        self.velocidade = velocidade
        self.ligado = ligado
        self.automatico = automatico

    def ligar(self, ligar):
        if ligar == 1:
            self.ligado = ligar
            print('O carro foi ligado')        
        else:
            print('Estado incorreto')

    def desligar(self, ligar):
        if ligar == 0:
            self.ligado = ligar
            print('O carro foi desligado')
        else:
            print('Estado incorreto')

    def acelerar(self, velocidade):
        if velocidade < 0:
            print('Velocidade inválida')
        elif velocidade > 120:
            print('Velocidade acima do suportado pelo carro')
        else:
            self.velocidade = velocidade

    def verificar_marcha(self, velocidade):
        if velocidade > 60:
            print('5ª marcha')
        elif velocidade > 45:
            print('4ª marcha')
        elif velocidade > 30:
            print('3ª marcha')
        elif velocidade > 20:
            print('2ª marcha')
        elif velocidade > 0:
            print('1ª marcha')
    
