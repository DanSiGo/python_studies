# 11. Crie uma lista com os nomes dos super-heróis que devem participar da Iniciativa Vingadores 
# seguindo a ordem: 
# • Homem de Ferro 
# • Capitão América 
# • Thor 
# • Hulk 
# • Viúva Negra 
# • Gavião Arqueiro

# a. Agora, inclua o Homem-Aranha no final da lista e imprima em qual posição está o Thor.
# b. Infelizmente a Viúva Negra e o Homem de Ferro não fazem mais parte da Iniciativa Vingadores, 
# então retire-os da lista.

herois = ['Homem de Ferro', 'Capitão América', 'Thor', 'Hulk', 'Viúva Negra', 'Gavião Arqueiro']

herois.append('Homem-Aranha')
print(herois)
print("Índice do Thor:", herois.index('Thor'))

herois.remove('Viúva Negra')
herois.remove('Homem de Ferro')

print(herois)