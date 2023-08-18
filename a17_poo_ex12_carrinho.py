'''
Crie uma classe CarrinhoDeCompras onde os atributos serão duas listas, uma para os produtos e outra para seus 
respectivos preços, se o cliente é VIP ou não e o total da compra que deve ser iniciado com 0.0.
Em seguida, crie os métodos para adicionar produtos ao carrinho e o exibir total da compra, que deverá imprimir 
em tela todos os produtos, os preços e, por fim, o total. Se o cliente for VIP, a compra terá 10% de desconto.
'''

class CarrinhoDeCompras:
    def __init__(self, vip, total):
        self.produtos = []
        self.precos = []
        self.vip = vip
        self.total = total
    
    def adicionar_produtos(self):
        while True:
            produto = input('Informe o produto para adicionar, ou 0 para sair: ')            
            if produto == '0':
                break
            self.produtos.append(produto)
            if self.vip == 1:
                self.precos.append(float(input('Informe o preço do produto: ')) * 0.9)
            else: 
                self.precos.append(float(input('Informe o preço do produto: ')))
    
    def exibir_total(self):
        for i in range(len(self.produtos)):
            print(f'Produto: [ {self.produtos[i]} ]', end = ' ')
            print(f'Preço: [ R$ {self.precos[i]} ]')

        total = 0
        for i in self.precos:
            total += i
        print(f'O total da compra foi: [ R$ {total} ]')

cliente_1 = CarrinhoDeCompras(1, 0)

cliente_1.adicionar_produtos()

cliente_1.exibir_total()