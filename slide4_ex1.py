n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1+n2+n3+n4)/4

print(media)
print("Média: ", round(media))

if media >= 7:
    print("A média foi maior ou igual a 7, aluno aprovado")
else:
    print("A média foi menor que 7, aluno reprovado")
