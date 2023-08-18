# peixe acima de 50kg leva multa de R$ 4.00 por kg excedente
# programa: receber o peso, calcular o excesso e o valor da multa

pescou = int(input("Digite o peso pescado: "))
excesso = pescou - 50
multa = excesso * 4

print("Foi pescado %.2fkg, havendo excesso de %.2fkg, resultando uma multa de R$%.2f" %(pescou, excesso, multa))





