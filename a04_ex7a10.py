# 7 - ler nome, endereço e telefone e ao final imprimir
nome = input("Digite o nome do cliente: ")
endereco = input("Digite o endereço do cliente: ")
telefone = input("Digite o telefone do cliente: ")

print("O cliente %s possui endereço em %s e seu telefone é %s" %(nome, endereco, telefone))

# 8 - ler três números reais, calcular a média aritmética e imprimir
n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
n3 = int(input("Digite o 3º número: "))
media = (n1 + n2 + n3)/3
print("A média dos número digitados é: %.2f" %media)

# 9 - ler dois números reais e faça as 4 operações e imprima
n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))

soma = n1 + n2
subt = n1 - n2
mult = n1 * n2
divi = n1 * n2

print("O resultado da soma dos número é: %d\nO resultado da subtração do primero pelo segundo é: %d\nO resultado da multiplicação é: %d\nO resultado da divisa é %.2f" %(soma, subt, mult, divi))

# 10 - converter um valor em dólar para real, deve mostrar o valor da cotação
cotacao_dolar = 5.06
dolar = float(input("Digite o valor em dólar para converter para real: "))
em_real = dolar * cotacao_dolar

print("O valor USD$%.2f convertido para real, utilizando a cotação de R$%.2f por dólar, é de R$%.2f" %(dolar, cotacao_dolar, em_real))




