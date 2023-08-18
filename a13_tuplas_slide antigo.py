'''
#######
# EXERCÍCIOS DO SLIDE INICIAL DE LISTAS
#######

lista = []

for x in range(16):
    lista.append(x)

print(lista[1:10])

tupla = tuple(lista)

print(tupla[1:10])
print(tupla[8:14])

print(tupla[0::2])

for x in tupla:
    if x % 2 == 0:
        print(x, end = ', ')

print()
print(tupla[1::2])

for x in tupla:
    if x % 2 != 0:
        print(x, end = ' ')
print()
for x in tupla:    
    if x % 2 == 0:
        print(x, end = ' ')
    elif x % 3 == 0 or x % 4 == 0:
        print(x, end = ' ')
    elif x % 4 == 0:
        print(x, end = ' ')
print()
print(tupla[::-1])

print(float(sum(list(tupla[10:])) / sum(list(tupla[3:10]))))
'''
