vazamentos = int(input("Informe quantos vazamentos foram notificados: "))
litros_perdidos = 0

for i in range(1, vazamentos+1):
    litros_hora = int(input(f"Informe a quantidade de litros perdidos por hora no {i}º vazamento: "))
    horas = int(input(f"Informe a quantidade de horas que o {i}º vazamento ficou aberto: "))
    litros_perdidos += litros_hora * horas

print(f"Ao total foram perdidos {litros_perdidos} litros de agua com os vazamentos")