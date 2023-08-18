n = int(input("Digite um número para calcular o fatorial: "))

i = 1
fat = 1

while i <= n:
    fat = fat * i
    i = i + 1

print("O fatorial de %d é" %(n), fat)
