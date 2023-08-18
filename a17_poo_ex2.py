class Funcionario:
    nome = None
    salario = None    

    def __init__(self, n, s):
        self.nome = n
        self.salario = s

    def aumentar_salario(self, percentual):
        return self.salario * (1 + (percentual/100))
    

func = input('Informe o nome do funcionário: ')
sala = float(input('Informe o salário do funcionário: '))
porcentagem = float(input('Informe o percentual de aumento: '))

func_1 = Funcionario(func, sala)
print(f'O salário reajustado do funcionaro {func_1.nome} é {func_1.aumentar_salario(porcentagem)}')