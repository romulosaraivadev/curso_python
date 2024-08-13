'''
iterável -> str, range, etc (__iter__)
iterador -> quem save entregar um valor po vez
next -> me entrega o próximo valor
iter -> me entrega seu iterador
'''
# texto = iter('Luiz') # __iter__()
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(next(texto))
texto = 'Romulo' # iterável
'''
# o for faz exatamente isso:

iterador = iter(texto) # iterador

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break
'''

for letra in texto:
    print(letra)