# 1. Faça um programa que leia a base e a altura de um retângulo e imprima o perímetro, a área e a diagonal. 
# Para fazer os cálculos, implemente três funções, cada uma deve realizar um cálculo especifico conforme solicitado. 
# Utilize as fórmulas a seguir.
import math

def calcular_perimetro(base, altura):
    perimetro = 2 * (base + altura)
    return perimetro

def calcular_area(base, altura):
    area = base * altura
    return area

def calcular_diagonal(base, altura):
    diagonal = math.sqrt(base**2 + altura**2)
    return diagonal

# 2. Construa um programa que leia um valor inteiro e retorne se a raiz desse número é exata ou não. 
# Escreva uma função para fazer a validação. Ao final imprima o resultado.

def raiz_inteira(x):
    raiz = math.sqrt(x)
    int_raiz = int(raiz)
    sera_decimal = raiz - int_raiz
    
    if sera_decimal == 0 :
        return 'Raiz exata'

