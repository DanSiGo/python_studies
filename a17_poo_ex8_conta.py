class ContaCorrente:
    def __init__(self, agencia, conta, saldo, favorecido):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.favorecido = favorecido

    def depositar(self, deposito):
        if deposito > 0:
            self.saldo += deposito
        else:
            print("Operação inválida")
        return self.saldo

    def sacar(self, saque):
        if 0 < saque <= self.saldo:
            self.saldo -= saque
        else:
            print("Operação inválida")
        return self.saldo

    def transferir(self, valor, destino):
        if 0 < valor <= self.saldo and destino != self.conta:
            self.saldo -= valor
            destino.depositar(valor)
        else:
            print("Operação inválida")

    def get_info(self):
        print(f'Dados da conta: ag. [ {self.agencia} ], cc: [ {self.conta} ], saldo: [ R$ {self.saldo} ]')

'''
agencia = 1 # int(input('Informe o numero da agência: '))
conta = 2 # int(input('Informe o número da conta: '))
saldo = 30.0 # float(input('Informe o saldo: '))
favorecido = 'daniel' # input('Informe o nome do favorecido: ')
'''

conta_1 = ContaCorrente(1, 2, 30.0, 'ana')
conta_2 = ContaCorrente(3, 4, 60.0, 'bruno')

conta_1.depositar(10.0)
conta_1.depositar(50.0)
conta_1.sacar(20)

conta_2.depositar(10.0)
conta_2.depositar(50.0)
conta_2.sacar(20)

conta_1.get_info()
conta_2.get_info()

conta_2.transferir(100, conta_1)

conta_1.get_info()
conta_2.get_info()


