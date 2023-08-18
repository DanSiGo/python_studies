# 1 - Faça um programa que leia três números e, para cada um, imprimir o dobro. O cálculo deverá
# ser realizado por uma função e o resultado impresso ao final do programa.
'''
def dobros(n1, n2, n3):
    print(f'O dobro de {n1} e {n1*2}')
    print(f'O dobro de {n2} e {n2*2}')
    print(f'O dobro de {n3} e {n3*2}')

   
dobros(int(input('informe o primeiro numero: ')), int(input('informe o segundo numero: ')), int(input('informe o terceiro numero: ')))
'''
# 2 - Faça um programa que receba as notas de três provas e calcule a média. Para o cálculo, escreva
# uma função. O programa deve imprimir a média ao final.
'''
def media(x):
    soma = 0
    for i in x:
        soma += i
    print(soma/len(x))
    
# notas = [i for i in range(3) input()]

notas = []

for i in range(3):
    nota = int(input(f'Informe a {i+1}º nota: '))
    notas.append(nota)

media(notas)
'''
# 3 - Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas vendas
# oferecendo desconto. Faça um programa que permita entrar com o valor de um produto e o
# percentual de desconto e imprimir o novo valor com base no percentual informado. Para fazer o
# cálculo, implemente uma função.
'''
def desconto(x, y):
    return x - (x * y / 100)
    # print(f'O valor com desconto e: {x - (x * y / 100)}')
    
valor = int(input('Informe o valor do item: '))
percentual = int(input('Informe o percentual de desconto: '))



print( f'O valor com desconto e: {desconto(valor, percentual)}')
'''
# 4 - Faça um programa que leia o saldo e o % de reajuste de uma aplicação financeira e imprimir o
# novo saldo após o reajuste. O cálculo deve ser feito por uma função.

# 5 - Faça um programa que verifique quantas vezes um número é divisível por outro. A função deve
# receber dois parâmetros, o dividendo e o divisor. Ao ler o divisor, é importante verificar se ele é
# menor que o dividendo. Ao final imprima o resultado.
'''
def quantas_divisoes(numero, divisor):
    contador = 0    
    while numero < divisor:
        numero = numero // divisor        
        contador += 1
    return contador
        
print(quantas_divisoes(int(input('informe o primeiro numero')), int(input('informe o segundo numero'))))

# Resposta da profa:

def verificar(dividendo,divisor):
    i = 0
    while dividendo>=divisor:
        dividendo=dividendo/divisor
        i+=1
    return i

dividendo = int(input("Informe o dividendo: "))
divisor = int(input("Informe o divisor: "))
print("Resultado: ", verificar(dividendo,divisor))
'''



