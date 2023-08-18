"""
UTILIZANDO FOR

Em um campeonato Europeu de Volleyball, se inscreveram 30 países. Sabendo-se que na lista oficial de cada país 
consta, além de outros dados, peso e idade de 12 jogadores, crie um programa que apresente as seguintes 
informações: 

• O peso médio e a idade média de cada um dos times; 
• O atleta mais pesado de cada time; 
• O atleta mais jovem de cada time; 
• O peso médio e a idade média de todos os participantes. 

"""
soma_peso = soma_idade = mais_pesado = peso_total = idade_total = jogadores_total = 0
mais_novo = 100

for pais in range(1, 5):
    print(f"\nTime >>> {pais} <<<")
    for jogador in range(1, 3):        
        peso = float(input(f"\nInforme o peso do jogador {jogador}: "))
        idade = int(input(f"Informe a idade do jogador {jogador}: "))
        soma_peso = soma_peso + peso
        soma_idade = soma_idade + idade

        if peso > mais_pesado:
            mais_pesado = peso
            jogador_mais_p = jogador
        
        if idade < mais_novo:
            mais_novo = idade
            jogador_mais_novo = jogador

        peso_total = peso_total + peso
        idade_total = idade_total + idade
        jogadores_total = jogadores_total + 1
    
    print(f"\nO peso médio do time {pais} é {soma_peso / jogador}kg\nA idade média do time {pais} é {soma_idade / jogador} anos")
    print(f"O atleta mais pesado do time {pais} é o joagador {jogador_mais_p} com peso {mais_pesado}kg")
    print(f"O atleta mais novo do time {pais} é o jogador {jogador_mais_novo} com a idade de {mais_novo} anos")

    soma_peso = 0
    soma_idade = 0
    mais_novo = 100
    
print(f"O peso médio de todos os participantes é: {peso_total / jogadores_total}")
print(f"A idade média de todos os participantes é: {idade_total / jogadores_total}")