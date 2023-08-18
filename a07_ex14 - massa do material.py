"""
WHILE ANINHADO 

Na Usina de Angra dos Reis, os técnicos analisam a perda de massa de um material radioativo. 
Sabendo-se que este perde 25% de sua massa a cada 30 segundos, criar um programa em Python que imprima o tempo necessário para que a 
massa deste material se torne menor que 0,10 grama. O programa deve calcular o tempo para várias massas.

"""
massa = 1
tempo = 0
while massa > 0:
    massa = float(input("Digite a massa do material. Digite 0 para encerrar: "))
    if massa == 0:
        break
    material = input("Informe o nome do material: ")    
    
    while massa > 0.10:
        massa = massa - (massa * 0.25)
        tempo = tempo + 30    
        
    print(f"O tempo necessário para o material {material} atingir menos de 0,10 gramas foi de {tempo} segundos")

    print("horas:", (tempo // 60)//60)
    print("minutos:", (tempo // 60) % 60)
    print("segundos:", tempo % 60)