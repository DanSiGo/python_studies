"""
2. Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua 
posição na lista. 
3. Ler uma lista de 10 números reais e mostre-os na ordem inversa. 
4. Ler uma lista com 4 notas, em seguida o programa deve exibir as notas e a média. 
5. Ler uma lista com 20 idades e exibir a maior e menor.
6. Faça um programa que armazene 10 letras em um vetor e imprima uma listagem numerada.
"""
"""
2. 

lista = []

for i in range(5):
    numero = int(input(f'Informe o {i+1}º um número inteiro: '))
    lista.append(numero)

lista = [5, 4, 6, 8, 7]
print(lista)
for i, p in enumerate(lista):
    print(i, p)
"""
"""
3. 
lista = []
for i in range(5):
    numero = int(input(f'Informe o {i+1}º um número inteiro: '))
    lista.append(numero)

lista.reverse()
print(lista)
"""
"""
4.
lista = []

for i in range(4):
    numero = int(input(f'Informe a {i+1}ª nota: '))
    lista.append(numero)

print(f"As notas são: {lista} e a média é {sum(lista)/len(lista)}")
"""
"""
lista = [22,54,66,32,14,78,52,21]
print(f"Maior idade da lista: {max(lista)}")
print(f"Menor idade da lista: {min(lista)}")
"""
"""
lista = ['a','b','c','d','e','f','g','h','i','j']
for i, x in enumerate(lista):
    print(i+1, x)
"""
