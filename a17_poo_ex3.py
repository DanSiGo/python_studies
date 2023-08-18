class Livro:
    
    def __init__(self, nom, pag, aut, pre):
        self.nome = nom
        self.paginas = pag
        self.autor = aut
        self.preco = pre

    def get_preco(self):
        return self.preco

    def set_preco(self, p):
        self.preco = p

livro_1 = Livro('harry potter', '300', 'Rowling', 40)

print(livro_1.get_preco())

livro_1.set_preco(60)
print(livro_1.get_preco())