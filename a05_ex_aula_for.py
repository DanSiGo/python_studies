"""
# programa, numeros de 5 a 100, divisiveis por 7 e nao por 5

for i in range(5, 101):
    if i % 7 == 0 and i % 5 != 0:
        print(f"Número divisível por 7, mas não por 5: {i}")

# recebe numero, calcula soma de todos os numeros de 1 ao digitado
"""
n = int(input("digite um numero: "))
soma = 0
for i in range (1, (n+1)):
    soma = soma + i
print(f"A soma dos números até o número informado é {soma}")