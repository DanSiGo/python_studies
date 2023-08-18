# ex 01) 
# Faça um programa que leia 3 números e imprima o maior deles.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    print("O maior número informado é o %d" %n1)
elif n2 > n1 and n2 > n3:
    print("O maior número informado é o %d" %n2)
elif n3 > n1 and n3 > n2:
    print("O maior número informado é o %d" %n3)

# ex 02) 
# Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores para cada estado. 
# Sabendo-se que os arqueiros de uma equipe não obtiveram o mesmo número de pontos, criar um programa 
# que informe se uma equipe foi classificada, de acordo com a seguinte especificação: 
# Ler os pontos obtidos por cada jogador da equipe;  
# Mostrar esses valores em ordem decrescente; 
# Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles, 
# caso contrário, imprimir a mensagem "Equipe desclassificada". 

eq1 = []
i = 0

while i < 3:
    i += 1
    nota = int(input("Digite a nota do jogador %d: " %i))
    eq1.append(nota)    
print("As notas da equipe 1 em ordem crescente é: ", sorted(eq1))

soma = 0
for i in eq1:
    soma = soma + i

if soma > 100:
    print("A média da equipe é: {}".format(soma/3))
else:
    print("Equipe desclassificada")

# ex 03) 
# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
 
n = 0

while n < 50:
    n += 1
    if n % 2 != 0:
        print(n)
