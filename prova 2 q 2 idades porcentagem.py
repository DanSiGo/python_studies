
idade = 0
a15 = 0
a30 = 0
a45 = 0
a60 = 0
a61 = 0

i = 1

while i <= 6:
    idade = int(input("Digite a idade da pessoa: "))
    
    if idade <= 15:
        a15 = a15 + 1
    elif idade <= 30:
        a30 = a30 + 1
    elif idade <= 45:
        a45 = a45 + 1
    elif idade <= 60:
        a60 = a60 + 1
    elif idade > 60:
        a61 = a61 + 1
    i = i + 1

porcentagem = (100/(i-1))

print("A quantidade de pessoas com idade até 15 anos é de:", a15, "e corresponde a", round(porcentagem * a15,2),"% do total de pessoas")
print("A quantidade de pessoas com idade até de 16 a 30 anos é de:", a30, "e corresponde a",round(porcentagem * a30,2), "% do total de pessoas")
print("A quantidade de pessoas com idade até de 31 a 45 anos é de:", a45, "e corresponde a",round(porcentagem * a45,2), "% do total de pessoas")
print("A quantidade de pessoas com idade até de 46 a 60 anos é de:", a60, "e corresponde a",round(porcentagem * a60,2), "% do total de pessoas")
print("A quantidade de pessoas com idade acima de 61 anos é de:", a61, "e corresponde a",round(porcentagem * a61,2), "% do total de pessoas")
