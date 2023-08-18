# Dada uma tupla T de n valores inteiros, escreva um programa que remova todos os números pares da tupla.

# t = [int(n) for n in input().split()]  # Esse é um método utilizado para criar uma lista com apenas 1 input, 
# voce informa todos os números de uma vez informando espaço entre os números, e dando apenas um enter

t = (1,2,3,2,4,5,6,4,2,6,7,5,6,7,8,9,9,6,7,8,12,12,2,13,14,14)
t = list(t)

for i in range(len(t), 0, -1):    
    if t[i-1] % 2 == 0:
        t.remove(t[i-1])
        
print(tuple(t))

# Dadas duas tuplas P1 e P2, ambas com n valores reais que representam as notas de uma turma na prova 1 e na prova 2, 
# respectivamente, escreva um programa que calcule a média da turma nas provas 1 e 2, imprimindo em qual das provas a
# turma obteve a melhor média.



# Dadas duas tuplas L1 e L2, com n e m valores inteiros, respectivamente, escreva um programa que concatene as tuplas
# L1 e L2 em uma nova tupla L3. Em seguida, imprima a tupla L3 ordenada de maneira crescente e decrescente.
