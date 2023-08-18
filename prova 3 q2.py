print("Digite sua idade em anos, meses e dias.")
ano = int(input("Anos: "))
mes = int(input("Meses: "))
dia = int(input("Dias: "))

em_dias = ((ano*365)) + (mes*30) + dia

print(em_dias)