n = int(input("Digite um número de 1 a 100: "))

i = 1
cont = 0

while i <= n:
    if n % i == 0:
        cont = cont + 1
    i = i + 1

if cont > 2:
    print("Não é primo")
elif cont == 2:
    print("É primo")