salario = float(input("Digite o salário: "))


if salario >= 1500:
    salario = salario * (105 / 100)
if 1500 >= salario > 700:
    salario = salario * (110 / 100)
if 700 >= salario >= 280:
    salario = salario * (115 / 100)
if salario <= 280:
    salario = salario * (120 / 100)

print(round(salario, 2))

   
