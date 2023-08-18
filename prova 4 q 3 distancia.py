distancia = 0
ligado = 1

print("Para calcular o trajeto, utilize os comandos: 'siga em frente', 'vire a esquerda', 'vire a direita' ou 'parar' ")

while ligado == 1:
    
    comando = str(input("Informe o comando: "))
    if comando == 'parar':
        ligado = 0
    elif comando == 'siga em frente' or comando == 'vire a esquerda' or comando == 'vire a direita':
        distancia += 100
    else:
        print("Você digitou um comando inválido")

print(f"Distância percorrida = {distancia/1000} Km")