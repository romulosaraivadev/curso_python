'''
Cuidados com dados mutaveis 
= - copiando o valor (imutaveis)
= - aponta para o mesmo valor na memória (mutável)
'''
lista_a = ['romulo', 'saraiva']
lista_b = lista_a.copy()

lista_a[0] = 'qualquer coisa'
print(lista_a)
print(lista_b)
