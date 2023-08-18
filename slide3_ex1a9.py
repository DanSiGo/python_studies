"""

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1+n2+n3)/3

print("A média das notas é: %.2f" %(media))
"""


# ex9 - dois numeros, fazer as 4 operações

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("A soma dos dois números é: ")
print("%.2f + %.2f = " %(n1, n2), n1+n2)

print("A subtração do primeiro número pelo segundo é: ")
print("%.2f - %.2f = " %(n1, n2), n1-n2)

print("A multiplicação do primeiro número pelo segundo é: ")
print("%.2f * %.2f = " %(n1, n2), f'{(n1*n2):.2f}')

print("A divisão do primeiro número pelo segundo é: ")
print("%.2f / %.2f = " %(n1, n2),f'{(n1/n2):.2f}')


