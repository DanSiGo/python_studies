# 01. Crie um dicionário d e coloque nele seus dados: nome, idade, telefone, endereço;
'''
meus_dados = {
    "Nome": "Daniel",
    "Idade": "35 anos",
    "Telefone": 85992783060,
    "Endereço": "R Henriqueta Galeno, 1040, 703"
}

for x, y in meus_dados.items():
    print(x,y)

print()
'''
# 02. Usando o dicionário d criado anteriormente, imprima seu nome;
'''
print(meus_dados.keys())
print(meus_dados["Nome"])
'''
# 03. Crie um dicionário dict e coloque nele os dados fornecidos pelo usuário: nome, idade, telefone, endereço;
'''
dados_usuario = {}

while True:
    nome = input("Informe seu nome (digite 0 para sair): ")
    if nome == "0":
        break
    idade = input("Informe sua idade: ")
    telefone = input("Informe seu telefone: ")
    endereco = input("Informe seu endereço: ")
    dados_usuario.update({"Nome:": nome, "Idade:": idade, "Telefone:": telefone, "Endereço:": endereco})
'''
# 04. Também usando dict, imprima todos os itens do dicionário no formato chave : valor, ordenado pela chave;
'''
for x, y in dados_usuario.items():
    print(x, y)
'''
# 05. Crie um programa que, usando dicionário, crie uma agenda de tamanho fornecido inicialmente pelo usuário. 
#   Leia os dados (nome, telefone) de todos os contatos do usuário de forma que a agenda fique completa e por 
#   fim imprima todos os contatos. Por fim, faça uma pesquisa pelo nome e apresente o telefone.
'''
agenda = {}
n = int(input('Informe a quantidade de nomes na agenda: '))

for i in range(n):
    nome = input("Informe o nome do contato: ")
    telefone = input('Informe o telefone: ')
    agenda.update({nome : telefone})

print(agenda)
for x, y in agenda.items():
    print(x,y)

contato = input('Digite o nome do contato para buscar: ')
print(agenda.get(contato))
'''
# 06. Crie um programa que armazena um grupo de 3 pessoas contendo o número de telefone de cada uma e a idade 
#   de cada uma e depois mostre todas as informações e a informação apenas de uma pessoa. 

agenda = {}

for i in range(3):
    nome = input(f'Informe o nome do {i+1}º contato: ')
    telefone = input('Informe o telefone: ')
    idade = input('Informe a idade: ')
    agenda.update({nome:{'Nome:': nome, 'Telefone': telefone, 'Idade:': idade}})

print(agenda.get(input('Informe o nome do contato para buscar: ')))


# RESPOSTA DA PROFESSORA:
'''
meusContatos = {}

for i in range (1,4):
    nome = input('Digite seu nome: ')
    tel = int(input('Digite seu telefone: '))
    idade = int(input('Digite sua idade: '))
        
    meusContatos [nome] = {} 
    meusContatos [nome] ['Telefone'] = tel
    meusContatos [nome] ['Idade'] = idade

for x, y in meusContatos.items():
    print(x, '=>', y)

print(meusContatos)

contato = input('Informe o nome do contato: ')

pesquisarContato = meusContatos.get(contato)

print(f'Contato do {contato}: {pesquisarContato}')
'''



