# ex 04) 
# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do 
# usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

i = 0
while i == 0:
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    if usuario == senha:
        print("A senha não pode ser igual ao nome de usário. Repita a operação.")
    else:
        i = 1

# ex 05)
# Faça um programa que leia 5 números e informe a soma e a média dos números.

i = 0
soma = 0
while i < 5:
    soma = soma + int(input("Digite um número para somar: "))
    i += 1

print("A soma dos número informados é: %d" %soma)
print("A média dos número informados é: {}".format(soma/5))

# ex 06) 
# Em uma escola, os alunos das turmas do fundamental fizeram uma prova de matemática. 
# Cada turma possui um número de alunos. 
# Criar um programa que imprima: 
# • quantidade de alunos aprovados; 
# • média de cada turma; 
# • percentual de reprovados. 
# Obs.: Considere aprovado com nota >= 7.0

i = 1
soma = 0
quantos_alunos = 0
reprovados = 0

while i != 0:
    quantos_alunos += 1
    aluno = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno %s: " %aluno))
    if nota >= 7.0:
        print("O aluno %s está aprovado" %aluno)
    else: 
        reprovados += 1
    soma = soma + nota
    i = int(input("Quer informar outro aluno? 1 - Sim | 0 - Não "))

print("A turma teve {} alunos aprovados ".format(quantos_alunos - reprovados))
print("A média da turma foi: {}".format(soma/quantos_alunos))
# f-strings: f na frente da string e dentro: {():.2f}
print(f"A porcentagem de alunos reprovados foi: {((reprovados/quantos_alunos) * 100):.2f}")


######################################################################################
######################################################################################
