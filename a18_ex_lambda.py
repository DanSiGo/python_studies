
# area do triangulo = base * altura / 2
'''
a_triangulo = lambda base, altura : base * altura / 2

base = 2
altura = 4

print(a_triangulo(base, altura))
'''

# IMC = peso / (altura ** 2)
'''
imc = lambda peso, altura : peso / (altura ** 2)

peso = 72
altura = 1.68

print(imc(peso, altura))
'''

# foi lhe fornecido uma lista de raios, utilize MAP para criar uma lista com as areas dos circulos. pi * (r ** 2)
'''
import math

lista_raios = [5, 6, 7, 8, 9, 4]

lista_areas_circulos = list(map(lambda r: round(math.pi * (r ** 2), 2), lista_raios))

print(lista_areas_circulos)
'''

# 1. calcule o imc com duas listas
'''
pesos = [70, 78, 59, 66, 67]
alturas = [1.78, 1.79, 1.67, 1.55, 1.49]

imc = list(map(lambda p, h : round(p / (h ** 2), 2), pesos, alturas))
print(imc)
'''

# 2. crie uma lista de nomes completos atraves da função map
'''
nomes = ['joao', 'marcos', 'sabrina', 'mariana']
sobrenomes = ['silva', 'oliveira', 'sato', 'ferreira']

nomes_completos = list(map(lambda n, s : n + ' ' + s, nomes, sobrenomes))

print(nomes_completos)
'''
# função filter

alturas = [1.70,1.79,1.67,1.55,1.49]
pessoas_170 = list(filter(lambda altura: altura if altura >= 1.70 else False, alturas))
print(pessoas_170)

# exe: filtras lista de imcs para deixar somente os imcs entre 18.5 e 25

lista_imcs = [20.28,30.35,18.9,26.7,19.67]

imcs_18_25 = list(filter(lambda i : i if 18.5 <= i <= 25 else None, lista_imcs))

print(imcs_18_25)

# exe: filtrar lista de nomes para deixar nomes somente até 6 caracteres. Se possivel deixar todos os nomes com a primeira letra maiúscula

lista_nomes = ['joao', 'antonio', 'marcela', 'luana', 'amanda', 'lucas']

nomes_6car = list(filter(lambda nome: nome.capitalize() if len(nome) <= 6 else None, lista_nomes))

print(nomes_6car)


