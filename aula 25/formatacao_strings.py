"""
Formatação básica de strings
s - string
d - int
f - float
.<número de digitos>f
x ou X - Hexadecimal
(caractere) (><^) (quantidade)
> - esquerda
< - direita
^ - centro
Sinal - + ou -
ex.: 0>-100,.1f
convesion flags - !r __repr__ !s __str__ !a __asc__
"""

variavel = 'ABC'
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{-1000.1654154787461:+,.1f}')
print(f'{1000.1654154787461:+,.1f}')
print(f'{1000.1654154787461:0=+10,.1f}')
print(f'O hexadecimal de 1500 é `{1500:08X}')
print(f'{variavel!r}')