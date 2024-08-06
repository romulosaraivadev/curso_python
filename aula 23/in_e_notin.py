# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  r o m u l o
# -6-5-4-3-2-1
nome = 'romulo'
# print(nome[2])
# print(nome[-3])
# print('o' in nome) responde true ou false
# print('a' in nome)
# print('rom' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o qu deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else: 
    print(f'{encontrar} não está em {nome}')