'''
enumerate - enumera iteráveis (indices)
'''
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = enumerate(lista)

# for indice, nome in lista_enumerada:
     
#     print(indice, nome)

# for item in lista_enumerada:
#     indice, nome = item
#     print(indice, nome)

for tupla_enumerada in enumerate(lista):
    print('For da tupla')
    for valor in tupla_enumerada:
        print(f'\t{valor}')