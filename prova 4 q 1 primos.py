n1 = int(input("Digite o número inicial: "))
n2 = int(input("Digite o número limite: "))
contador = divisor = 0
while n1 <= n2:
    while divisor <= n1:
        divisor += 1
        if n1 % divisor == 0:
            contador += 1
    if contador == 2:
        print(n1)
    divisor = contador = 0
    n1 += 1
    