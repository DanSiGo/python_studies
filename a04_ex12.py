# quanto ganha por hora, horas trabalhadas no mês e mostre o total
# do salário no mês, desconta 11% de IR, 8% de INSS e 5% de 
# sindicato
# mostrar: 
# a) quanto pagou ao INSS
# b) quanto pagou ao sindicato
# c) salário líquido
# d) descontos e salário líquido mostrando:
# + Salário bruto: R$
# - IR (11%): R$
# - INSS (8%): R$
# - Sindicato (5%): R$
# = Salário Líquido: R$

sal_hora = int(input("Digite o valor do salário por hora trabalhada: "))
htrab_mes = int(input("Digite a quantidade de horas trabalhadas no mês: "))

sal_bruto = sal_hora * htrab_mes

print("+ Salário bruto: R$%.2f" %sal_bruto)
print("- IR (11%): R$", sal_bruto*0.11)
print("- INSS(8%): R$", sal_bruto*0.08)
print("- Sindicato: R$", sal_bruto*0.05)
print("= Salário Líquido: R$", sal_bruto - ((sal_bruto*0.11) + (sal_bruto*0.08) + (sal_bruto*0.05)))

