"""
# 8. Faça um programa que armazene 15 números inteiros em um vetor e depois permita que o 
# usuário digite um número inteiro para ser buscado no vetor, se for encontrado o programa deve imprimir 
# a posição desse número no vetor, caso contrário, deve imprimir a mensagem: "Nao encontrado!".

lista = []

for i in range(3):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista.append(numero)

qual = int(input("Digite qual número que encontra: "))

if qual in lista:
    print(f"O número {qual} está no índice {lista.index(qual)}")
else:
    print(f"O número {qual} não está na lista")
"""
"""

# 9. Faça um programa que armazene 8 números em uma lista e imprima todos os números. 
# Ao final, imprima o total de números múltiplos de seis. 

lista = []

for i in range(3):
    numero = int(input(f"Informe o {i+1}º numero: "))
    lista.append(numero)

for i in lista:
    if i % 6 == 0:
        print(f"O número {i} é múltiplo de 6")
    else: 
        print(f"O número {i} não é múltiplo de 6")
"""
# 10. Faça um programa que armazene as notas das provas 1 e 2 de 15 alunos. Calcule e armazene a média. 
# Armazene também a situação do aluno: 1- Aprovado ou 2-Reprovado. 
# Ao final o programa deve imprimir uma listagem contendo as notas, a média e a situação de cada aluno. 
# Utilize quantas listas forem necessárias para armazenar os dados.

notas = []
alunos = []
lista_media = []
situacao = []

nome = 'aluno'

while nome != 0:
    media = 0
    nome = input('Digite o nome do aluno: ')
    if nome == str(0):
        break

    alunos.append(nome)

    for i in range(2):
        nota = int(input(f"Informe a {i + 1}ª nota do aluno {nome}:"))
        notas.append(nota)
        media += nota/2
    
    lista_media.append(media)

    if media >= 7:
        situacao.append("APROVADO")
    else:
        situacao.append("REPROVADO")

for i in range(len(alunos)):
    n = i + 1
    if i == 0:
        print(f"{alunos[i]} possui as seguintes notas: {notas[i:n+1]}")
    else:
        print(f"{alunos[i]} possui as seguintes notas: {notas[n:n+2]}")
    
    print(f"A média do aluno {alunos[i]} foi de {lista_media[i]}")
    print(f"A situação do aluno {alunos[i]} é {situacao[i]}")

