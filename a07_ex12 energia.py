"""
Uma empresa de fornecimento de energia elétrica faz a leitura mensal dos medidores de consumo. 
Para cada consumidor, são digitados os seguintes dados: 
• número do consumidor 
• quantidade de kWh consumidos durante o mês 
• tipo (código) do consumidor 
    1-residencial, preço em reais por kWh = 0,3 
    2-comercial, preço em reais por kWh = 0,5 
    3-industrial, preço em reais por kWh = 0,7 

Os dados devem ser lidos até que seja encontrado o consumidor com número 0 (zero). 

O programa deve calcular e imprimir: 
• O custo total para cada consumidor 
• O total de consumo para os três tipos de consumidor 
• A média de consumo dos tipos 1 e 2 
"""
numero_do_consumidor = 1
valor_kwh = consumo_1 = consumidor_1 = consumo_2 = consumidor_2 = consumo_3 = 0

while numero_do_consumidor > 0:
    numero_do_consumidor = int(input("Digite o número do consumidor. Digite 0 para encerrar: \n"))
    if numero_do_consumidor == 0:
        break
    consumo = float(input(f"Digite o consumo de kWh do consumidor {numero_do_consumidor}: \n"))    
    tipo_do_consumidor = int(input("Digite o tipo do consumidor: \n1 - residencial; \n2 - comecial; \n3 - industrial: \n"))    
    if tipo_do_consumidor == 1:        
        consumo_1 = consumo_1 + consumo
        consumidor_1 = consumidor_1 + 1
    elif tipo_do_consumidor == 2:        
        consumo_2 = consumo_2 + consumo
        consumidor_2 = consumidor_2 + 1
    elif tipo_do_consumidor == 3:        
        consumo_3 = consumo_3 + consumo
    else:
        print("\nVocê digitou um tipo de consumidor inválido, tente de novo.\n")
        continue   

print(f"\nO custo total para o consumidor residencial foi de R$ {consumo_1 * 0.3}")
print(f"O custo total para o consumidor comercial foi de R$ {consumo_2 * 0.5}")
print(f"O custo total para o consumidor industrial foi de R$ {consumo_3 * 0.7}")

print(f"\nO total de consumo residencial foi de {consumo_1}")
print(f"O total de consumo comercial foi de {consumo_2}")
print(f"O total de consumo industrial foi de {consumo_3}")

if consumidor_1 == 0:
    consumidor_1 = 1

if consumidor_2 == 0:
    consumidor_2 = 1

print(f"\nA média de consumo do tipo 1 foi de {consumo_1 / consumidor_1}")
print(f"A média de consumo do tipo 2 foi de {consumo_2 / consumidor_2}")


    