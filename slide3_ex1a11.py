pescou = int(input("Digite o peso pescado: "))

if pescou > 50:
    excesso = (pescou-50)
    multa = excesso * 4
    print("O pescador pescou %.2f kg e recebeu uma multa de R$ %.2f referente a %.2f kg pescados a mais" % (pescou, multa, excesso))


