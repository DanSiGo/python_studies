# EX 1
# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

i = 4
soma = 0

while i > 0:
    nota = int(input("Digite uma nota para somar à média: "))
    soma = soma + nota
    i -= 1

print("A média das notas é: {media}".format(media = (soma/4)))

# EX 2
# Faça um programa que leia dois valores numéricos inteiros e efetue 
# a adição, caso o resultado seja maior que 10, apresentá-lo.

n1 = 3
n2 = 8

if (n1+n2) > 10:
    print(n1+n2)

# EX 3
# Faça um programa que leia dois valores inteiros e efetue a adição. 
# Caso o valor somado seja maior que 20, este deverá ser apresentado 
# somando-se a ele mais 8, caso o valor somado seja menor ou igual a 20, 
# este deverá ser apresentado subtraindo-se 5.

n1 = 3
n2 = 8

if (n1+n2) > 20:
    print((n1+n2) + 8)

else:
    print((n1+n2) - 5)

# EX 4
# Faça um programa que leia um número e imprima uma das duas mensagens: 
# "É múltiplo de 3"ou "Não é múltiplo de 3". 

n = int(input('Digite um número: '))

if n % 3 == 0:
    print("é múltiplo de 3")

else:
    print("não é múltiplo de 3")

# EX 5
# Faça um programa que leia um número e informe se ele é divisível 
# por 3 e por 7.

n = int(input("digite um número: "))

if (n % 3 == 0) and (n % 7 == 0):
    print("é divisível por 3 e por 7")

else:
    print("não é divisível por 3 e por 7")

# EX 6
# Faça um programa em C que permita entrar com o ano de nascimento 
# da pessoa e com o ano atual. O programa deve imprimir a idade da 
# pessoa. Não se esqueça de verificar se o ano de nascimento informado 
# é válido.

i = 0

while i == 0:
    ano = int(input("Digite o ano atual: "))
    nasc = int(input("Informe o ano de nascimento: "))
    
    if (nasc >= 0) and (nasc <= ano):
        i = 1
    else:
        print("Você digitiou um ano inválido. Digite um ano entre 0 e %s\n") % ano

print("A diferença entre os anos é de:{}".format(ano - nasc))

# EX 7
# Depois da liberação do governo para as mensalidades dos planos de 
# saúde, as pessoas começaram a fazer pesquisas para descobrir um bom 
# plano, não muito caro. Um vendedor de um plano de saúde apresentou a 
# tabela a seguir. Faça um programa que entre com o nome e a idade de 
# uma pessoa e imprima o nome e o valor que ela deverá pagar.

idade = int(input("Digite a idade: "))

if idade < 10:
    print("Valor: R$30,00")
elif idade < 29:
    print("Valor: R$60,00")

elif idade < 45:
    print("Valor: R$120,00")

elif idade < 59:
    print("Valor: R$150,00")

elif idade < 65:
    print("Valor: R$250,00")

elif idade >= 65:
    print("Valor: R$400,00")
