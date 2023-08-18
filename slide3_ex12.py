sal_hora = float(input("Digite qual salário por hora: "))
horas_trab = float(input("Digite quantas horas trabalhou: "))

total_sal = sal_hora * horas_trab

ir = total_sal * 0.11
inss = total_sal * 0.08
sindicato = total_sal * 0.05

sal_liq = total_sal - ir - inss - sindicato


print("Seu salário bruto é: ", total_sal)
print("Pagou de INSS: ", inss)
print("Pagou de sindicato: ", sindicato)

print("O salário líquido é: R$%.2f" % sal_liq)

print("""
+ Salário Bruto: R$ %.2f
- IR (11): R$ %.2f
- INSS (8): R$ %.2f
- Sindicato (5): R$ %.2f
= Salário Líquido: R$ %.2f
""" 
% (total_sal, ir, inss, sindicato, sal_liq))
