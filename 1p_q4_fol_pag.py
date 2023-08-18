salario_hora = float(input("Digite o valor do salário por hora trabalhada: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))


salario_bruto = salario_hora * horas_trabalhadas

ir = salario_bruto * (5 / 100)
inss = salario_bruto * (10 / 100)
sindicato = salario_bruto * (3 / 100)
fgts = salario_bruto * (11 / 100)

total_descontos = ir + inss + sindicato

salario_liquido = salario_bruto - total_descontos

print(f"Salário Bruto ({salario_hora} * {horas_trabalhadas}): R$ {salario_bruto}\n(-) IR (5%): R${ir}\n(-) INSS (10%): R${inss}\n(-) Sindicato (3%): R${sindicato}\nFGTS (11%): R${fgts}\nTotal de descontos: R${total_descontos}\nSalário Líquido: R${salario_liquido}")                          
