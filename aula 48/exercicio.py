'''
Exercício
exiva os indeces da lista
 '''
# lista = ['Maria', 'Helena', 'Romulo']

# for indice, nome in enumerate(lista):
#     print(indice, nome)

lista = ['Maria', 'Helena', 'Romulo']
lista.append('João')
indice = range(len(lista))

for indices in indice:
    print(indices, lista[indices], type(lista[indices]))
