



n = int(input("Digite a quantidade de habitantes: "))
i = 1
hab = 0
homens = 0
mulheres = 0

while i <= n:
    hab = int(input("Digite o sexo do habitante %d, sendo 1 para homem e 2 para mulher: " %(i)))

    if hab == 1:
        homens = homens + 1

    if hab == 2:
        mulheres = mulheres + 1

    i = i + 1

print("Homens:", homens, "\nMulheres:", mulheres)
