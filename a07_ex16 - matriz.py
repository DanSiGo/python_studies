"""
FOR ANINHANDO

Faça um programa em Python que imprima uma matriz de 4 linhas por 4 colunas, sendo que na primeira linha devem ser impressos os 
valores de 1 à 4 e partir da segunda linha, os valores impressos devem ser múltiplos da linha anterior.

"""

for i in range(1, 5):
    for x in range(1,5):
        print(f"{i*x :<5}", end = "")
    print("")
