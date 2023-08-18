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
#5 Ler uma lista com 20 idades e exibir a maior e menor.

lista = []
for i in range(3):
    idade = int(input("Digite a idade: "))
    lista.append(idade)

print(f"A menor idade é {lista(min)} e a maior é {lista(max)}")
"""
"""
#6 Faça um programa que armazene 10 letras em um vetor e imprima uma listagem numerada.

lista = []
for i in range(10):
    letras = input("Digite letras: ")
    lista.append(letras)
for i, p in enumerate(lista):
    print(i + 1, "=>", p)
"""
# 7 Ler uma lista de 15 números inteiros e mostre cada número juntamente com a 
# sua posição na lista

lista = []

for i in range(3):
    numero = int(input("Digite os números: "))
    lista.append(numero)

for i, p in enumerate(lista):
    print(f"O indice {i} corresponde ao número {p}")




