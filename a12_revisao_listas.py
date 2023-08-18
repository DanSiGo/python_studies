
# Reescreva o programa da questão anterior, mas agora armazenando os nomes e idades em duas listas 
# diferentes. Por fim, também apresente na tela as duas listas obtidas.
'''
nomes = [input(f'Digite o nome da {i+1}ª pessoa: ') for i in range(5)]
idades = [int(input(f'Digite a idade da {i+1}ª pessoa: ')) for i in range(5)]


for i in range(5):
    nomes.append(input(f'Digite o {i+1}º nome: '))
    idades.append(input(f'Digite a idade da {i+1}ª pessoa: '))
'''
'''
for i in range(5):
    print(f'Nome: {nomes[i]} - Idade: {idades[i]} anos')

print([f'Nome: {nomes[i]} - Idade: {idades[i]} anos' for i in range (5)])

# 466
# 527
# 060
# 08

print('466', '527', '060', sep='.', end='-08')
'''

# 4 Escreva um programa que peça o nome e a média de 10 alunos,
# Adicione à uma lista apenas os nomes dos alunos com média maior do que sete.
# Imprima em tela a lista dos aprovados.
'''
aprovados = []
for i in range(3):
    aluno = input(f'Digite o nome do {i+1}º aluno: ')
    media = int(input(f'Informe a média do aluno: '))
    if media >= 7:
        aprovados.append(aluno)

print(aprovados)
'''

# Crie um programa que peça dez números inteiros e positivos.
'''
Ao finalizar, informe separadamente:
1) a soma dos números pares
2) a soma dos números ímpares
3) o menor e o maior da lista de números pares
4) o menor e o maior da lista de números ímpares
5) a lista de números pares
6) a lista de números ímpares
7) Imprima ao final a lista completa



lista = [int(input(f'Digite o {i+1}º número: ')) for i in range(4)]
lista_pares = []
lista_impares = []
soma_par = soma_impar = 0

for i in lista:
    if i % 2 == 0:
        soma_par += i
        lista_pares.append(i)
    elif i % 2 != 0:
        soma_impar += i
        lista_impares.append(i)


print(f'A soma dos número pares é: {soma_par}')
print(f'A soma dos números ímpares é: {soma_impar}')
print(f'O menor número par é {min(lista_pares)} e o maior é {max(lista_pares)}')
print(f'O menor dos ímpares é {min(lista_impares)} e o maior é {max(lista_impares)}')
print(f'A lista de números pares é {lista_pares} e a dos ímpares é {lista_impares}')
print(f'A lista completa é {lista}')

'''

