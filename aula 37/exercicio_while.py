'''
Interado strings com while
'''
#       01234567891011
nome = 'Romulo Saraiva' # Iteráveis


indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice +=1
novo_nome += '*'
print(novo_nome)