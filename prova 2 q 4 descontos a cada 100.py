

valordacompra = int(input("digite o valor da compra: R$ "))
faixa = 500
desconto = 0

if  valordacompra >= 500:
    while faixa <= valordacompra:
        desconto = desconto + 1
        faixa = faixa + 100

valorfinal = valordacompra - (valordacompra*desconto/100)


print("O valor da compra foi: R$", valordacompra)
print("A porcentagem de desconto é de:", desconto, "%")
print("O valor final da compra com desconto aplicado é de: R%", valorfinal,"\n")


print(valordacompra, "(Valor da compra) -", desconto,"% (Porcentagem) =", valorfinal,"(Valor final)") 
