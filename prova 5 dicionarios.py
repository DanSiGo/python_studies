# A NASA (Agência Espacial dos Estados Unidos) mantém um registro de todos os asteroides e suas distâncias relativas da Terra. 
# Você foi convidado para escrever um código que leia o nome do asteróide (chaves do dicionário) e uma lista que contenha as  
# 5 últimas distâncias  do asteróide com a Terra. Lembre-se de que: distância são os valores do dicionário.

# Em seguida, armazene os dados coletados em um dicionário, onde a chave utilizada será o nome do asteróide, exibindo no final, 
# a distância média dos asteróides registrados com Terra.

# obs: use a função sum()

asteroides = {}
n_aster = media = 0

while True:
    n_aster += 1
    distancias = []
    aster = input(f'\nInforme o nome do {n_aster}º asteroide\nOu digite 0 para encerrar:\n\n')
    print()
    
    if aster == '0':
        break

    for i in range(1, 6):
        dista = float(input(f'Informe a {i}ª distância do asteroide {aster}: '))        
        distancias.append(dista)
    
    asteroides.update({aster: distancias})

print('='*20,'Resultados','='*20) 

for x, y in asteroides.items(): 
    
    print(f'\nAsteroide: {x}\n\nDistâncias: {y}') 
    print(f'A distância média do asteroide {x} com a terra é {sum(y)/len(y)}')

