import a15_modulo


base = int(input('Informe a base: '))
altura = int(input('Informe a altura: '))
valor = int(input('Informe um valor inteiro para calcular a raiz quadrada: '))

print(a15_modulo.calcular_area(base, altura))
print(a15_modulo.calcular_diagonal(base, altura))
print(a15_modulo.calcular_perimetro(base, altura))
print(a15_modulo.raiz_inteira(valor))