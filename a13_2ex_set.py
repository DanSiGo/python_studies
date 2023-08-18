# 1 Transforma a lista abaixo em um set: lista = [1,2,6,9,5,2]
lista = [1,2,6,9,5,2]
lista = set(lista)
print(lista)

# 2 Remova um elemento do conjunto e mostre qual foi excluído;

print(lista.pop())
print(lista)

# 3 Verifique se o número 9 existe no set;

if 9 in lista:
    print("Consta")
else:
    print("Não consta")

# 4 Adicione o número 10 ao conjunto;

lista.add(10)
print(lista)

# 5 Remova o item 5 do set;

lista.remove(5)
print(lista)

# 6 Crie uma cópia do conjunto;

nova_lista = lista.copy()
print(nova_lista)

# 7 Atualize um conjunto pela a união com outro conjunto.
outra_lista = {3,7,8,4,12}
nova_lista.update(outra_lista)
print(nova_lista)

# 8 Faça união do conjunto da questão 6 com da 7;

uniao = nova_lista.union(outra_lista)
print(uniao)

