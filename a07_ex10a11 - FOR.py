# Escreva um programa que mostre todos os números entre 5 e 100 que são divisíveis por 7, 
# mas não são múltiplos de 5. Os números obtidos devem ser impressos em sequência.

for i in range (5, 101):
    if (i % 7 == 0) and (i % 5 != 0):
        print(f"O número {i} é divisível por 7 e não é divisível por 5")

# Faça um programa que receba um número digitado pelo usuário e calcule a soma de todos os números de 1 até ao número digitado. 
# Por exemplo, se o usuário digitou o número 4, a saída deve ser 10 (1+2+3+4=10).

n = int(input("Digite um número: "))
soma = 0
for i in range (n + 1):
    soma = soma + i
print(f"A soma dos números de 1 até {n} é {soma}")