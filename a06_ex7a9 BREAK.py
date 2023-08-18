"""
# ex 07) 
# Uma pesquisa de opinião realizada no Ceará com 50 pessoas, teve as seguintes perguntas: 
# • Qual o seu time de coração? 1-Fortaleza; 2-Ceará; 3-Ferroviário; 4-Icasa; 5-Outros 
# • Onde você mora? 1-Fortaleza; 2-Caucaia; 3-Outros 
# • Qual o seu salário? 

# Faça um programa que imprima:
#  • o número de torcedores por clube; 
#  • a média salarial dos torcedores do Fortaleza; 
#  • o número de pessoas moradoras de Caucaia, torcedores do Ferroviário;
#  • o número de pessoas de Fortaleza torcedores do Ceará.
fort = 0
cear = 0
ferr = 0
icas = 0
outr = 0
salario_fortaleza = 0
caucaia_ferro = 0
fortal_ceara = 0
i = 0
while i < 5:
    i += 1
    time = int(input("\nQual o seu time de coração? \n1-Fortaleza; \n2-Ceará; \n3-Ferroviário; \n4-Icasa; \n5-Outros \n"))
    if time == 1:
        fort += 1
    elif time == 2:
        cear += 1
    elif time == 3:
        ferr += 1
    elif time == 4:
        icas += 1
    elif time == 5:
        outr += 1
    else:
        print("Voce digitou uma opção inválida.\n")
    mora = int(input("\nOnde você mora? \n1-Fortaleza; \n2-Caucaia; \n3-Outros \n"))
    if mora == 2 and time == 3:
        caucaia_ferro += 1
    elif mora == 1 and time == 2:
        fortal_ceara += 1
    sala = float(input("\nQual o seu salário:? \n"))
    if time == 1:
        salario_fortaleza = salario_fortaleza + sala

print(f"\na) Quantidade de torcedores:\nFortaleza = {fort}\nCeará = {cear}\nFerroviário = {ferr}\nIcasa = {icas}\nOutros = {outr}\n")
print(f"b) Média salarial torcedores do Fortaleza = {(salario_fortaleza/fort):.2f}\n")
print(f"c) Moradores de Caucaia torcedoras do Ferroviário = {caucaia_ferro}\n")
print(f"d) Moradores de Fortaleza torcedoras do Ceará = {fortal_ceara}\n")
    


# ex 08)
# Faça um programa em Python que leia um valor inteiro e mostre a tabuada de 1 a 10 do valor lido.
n = int(input("Digite o número: "))
for i in range(1, 11):    
    print(f"{n} x {i} = {n*i}")

"""
# ex 09) 
# Faça um programa que leia um nome de usuário e verifique se o mesmo esta contido na lista de 
# usuários criados, se estiver mostre uma mensagem com o nome.
lista = ["ana", "beatriz", "carlos", "daniel", "erick", "fernanda"]
nome = input("Digite seu nome: ")
if nome in lista:
        print("Seu nome está na lista")
for i in lista:    
    if nome == i:
        print("Com for in, seu nome está na lista")

# nessa aula explicou BREAK, CONTINUE, PASS:
# break para o laço
# continue suspende o laço, ou seja, não executa as instruções seguintes, apenas retorna para o inicio do laço novamente
# pass faz a condição ou laço apenas passar, evitando que dê algum problema ou erro