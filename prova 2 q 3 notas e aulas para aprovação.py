
n1 = int(input("Digite a nota 1: "))
n2 = int(input("Digite a nota 2: "))
n3 = int(input("Digite a nota 3: "))

presenca = int(input("Digite a quantidade de aulas que o aluno compareceu: "))
               
aulas = int(input("Digite a quantidade mínima de aulas para aprovação: "))

media = (n1 + n2 + n3) / 3

if (media >= 6) and (presenca >= 40):
    print("Aprovado")
else:
    print("Reprovado")
