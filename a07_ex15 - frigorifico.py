"""
FOR

Num frigorífico existem 90 bois. Cada boi traz preso em seu pescoço um cartão contendo seu número de identificação e seu peso. 
Faça um programa que imprima a identificação e o peso do boi mais gordo e do boi mais magro (supondo que não haja empates).

"""
maior_peso = 0
menor_peso = 10000
for boi in range(1, 5):
    identificacao = int(input("\nInforme o número de identificação do boi: "))
    peso = float(input("Informe o peso do boi: "))

    if peso > maior_peso:
        maior_peso = peso
        boi_gordo = identificacao

    if peso < menor_peso:
        menor_peso = peso
        boi_magro = identificacao

print(f"\nO boi mais gordo é o de número {boi_gordo}, pesando {maior_peso}")
print(f"O boi mais magro é o de número {boi_magro}, pesando {menor_peso}")
