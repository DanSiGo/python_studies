"""
Faça um programa em Python que efetue a apresentação do valor da conversão em real (R$) de um valor lido em dólar (US$). Para isso, será 
necessário também ler o valor da cotação do dólar. 

"""

em_dolar = float(input("Digite o valor em dolar: "))

cotacao = 5.20

em_real = em_dolar * cotacao

print("USD$ %.2f equivale a R$ %.2f, com a cotação de cada dólar valendo R$ %.2f" %(em_dolar, em_real, cotacao))
