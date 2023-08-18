# Construa um programa que realize as reservas de passagens áreas de uma companhia. 

# O programa deve permitir cadastrar o número de 10 voos e definir a quantidade de 
# lugares disponíveis para cada um. 

# Após o cadastro, leia vários pedidos de reserva, constituídos do número da carteira de 
# identidade do cliente e do número do voo desejado. 

# Para cada cliente, verificar se há possibilidade no voo desejado. Em caso afirmativo, 
# imprimir o número da identidade do cliente e o número do voo, atualizando o número de 
# lugares disponíveis. 
# 
# Caso contrário, avisar ao cliente a inexistência de lugares. 

# A leitura do número 0 (zero) para o voo desejado indica o término da leitura de reservas.

voo = []
lugares = []
clientes = []
voo_confirmado = []

for i in range(1):
    n_voo = int(input('Informe o número do vôo: '))
    voo.append(n_voo)
    q_lugares = int(input(f"Informe a quantidade de lugares disponíveis no voo {voo[i-1]}: "))
    lugares.append(q_lugares)

while True:
    cliente = int(input('Informe o número da identidade do cliente, ou 0 para encerrar: '))
    if cliente == 0:
        break

    if cliente != 0:
        while True:
            qual_voo = int(input('Informe o vôo desejado ou 0 para sair: '))
            if qual_voo == 0:
                break
            if qual_voo not in voo:
                print('O número do vôo informado é inválido')
                continue
        
            elif qual_voo in voo:
                if lugares[voo.index(qual_voo)] > 0:
                    print(f'Cliente RG nº {cliente} confirmado no vôo {qual_voo}')
                    clientes.append(cliente)
                    voo_confirmado.append(qual_voo)
                    lugares[voo.index(qual_voo)] -= 1
                    print(f'Assentos disponíveis no vôo {qual_voo} atualizado para {lugares[voo.index(qual_voo)]}')
                    break

                else:
                    print(f'O vôo {qual_voo} não possui assentos disponíveis')

print('\nClientes confirmados e seus respectivos vôos:\n')

for i in range(len(clientes)):
    print(f'Cliente: {clientes[i-1]} => Vôo: {voo_confirmado[i-1]}')

        

