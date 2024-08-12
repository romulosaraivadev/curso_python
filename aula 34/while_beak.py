'''
Repetições 
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
loop infinito -> quando um codigo não tem fim
'''
# condicao = True

# while condicao:
#     nome = input('Qual o seu nome: ')
#     print(f'Seu nome é {nome}')

#     if nome == 'sair':
#         break
# print('Acabou')

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6')
        continue

    if contador >= 10 and contador <= 27:

        continue

    print(contador)

    if contador == 40:
        break
    
print('Acabou')