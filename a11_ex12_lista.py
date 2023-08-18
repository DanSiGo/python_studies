# 12. Crie um programa que leia 5 números inteiros e os armazene em uma lista de tal forma que todos os 
# números maiores ou iguais que o primeiro fiquem ao lado direito e todos os menores fiquem ao lado 
# esquerdo.

lista = []

for i in range(5):
    numero = int(input("Informe um número: "))
    if len(lista) == 0:
        primeiro = numero
        lista.append(numero)
    
    elif numero > primeiro:        
        lista.insert(lista.index(primeiro)+i, numero)
        
    else:        
        lista.insert(lista.index(primeiro), numero)
        
# COMO DEIXAR OS ULTIMO NUMEROS ADICIONADOS MAIS PROXIMO DO 5?

print(lista)
