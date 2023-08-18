def subt(n1, n2):
    # if n2 > n1:
        # return n2-n1
    # else:
    return n1-n2

def soma(n1, n2):
    return n1 + n2
    
def mult(n1, n2):
    return n1 * n2
    
def divi(n1, n2):
    return n1 / n2

while True:
    operacao = int(input('Informe a operaçao desejada: \n1 - soma; \n2 - subtracao; \n3 - multiplicacao; \n4 - divisao; \n0 - sair: '))

    if operacao == 1:
        print(soma(int(input('Digite o primeiro numero: ')), int(input('Digite o segundo numero: '))))
        
    elif operacao == 2:
        print(subt(int(input('Digite o primeiro numero: ')), int(input('Digite o segundo numero: '))))
        
    elif operacao == 3:
        print(mult(int(input('Digite o primeiro numero: ')), int(input('Digite o segundo numero: '))))
        
    elif operacao == 4:
        print(divi(int(input('Digite o primeiro numero: ')), int(input('Digite o segundo numero: '))))
    else:
        break
    
    
