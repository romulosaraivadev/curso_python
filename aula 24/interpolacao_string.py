"""
Interpolação básica de strings
s - string
d e i - inteiro
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Romulo'
preco = 1000.95952345
variavel = '%s, o preço é R$%.2f ' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08x' % (1500, 1500))