'''
Introdução ao desempacotamento + tuples (tuplas)
'''


# nome1, nome2, nome3, nome4= ['Maria', 'Helena', 'Luiz']
# print(nome2)

_, _, nome1, *resto= ['Maria', 'Helena', 'Luiz']
print(nome1, _)