
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero = input('Digite um número inteiro: ')


# try:
#     numero_int = int(numero)
#     if numero_int % 2 ==0:
#         print('Seu número é par')
#     else:
#         print('Seu numero é impar')
# except:
#     print('O numero não é inteiro')

#resolução do professor

entrada = input('Digite um número inteiro: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'
    if par_impar:
        par_impar_texto = 'par'
        print(f'O número {entrada_int} é {par_impar_texto}')
else: 
    print('Vôce não digitou um número inteiro')
"""
Faça um programa que exige a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação correspondente. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# hora = input('Digite uma hora: ')
# hora_int = int(hora)

# if hora_int > 23:
#     print('Você digitou uma hora errada')
# elif hora_int <= 23 and hora_int > 18:
#     print('boa noite')
# elif hora_int <= 18 and hora_int > 12:
#     print('Boa tarde')
# elif hora_int <= 11:
#     print('Bom dia')

#resolução do professor
entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')
"""
Faça um programa que parte do primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
“Seu nome é normal”; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Digite seu nome: ')
nome_quantidade_letras = len(nome)

if nome_quantidade_letras <= 4:
    print('Seu nome é curto')
elif nome_quantidade_letras >= 5 and nome_quantidade_letras <= 6:
    print( 'Seu nome é normal')
elif nome_quantidade_letras > 6:
    print('Seu nome é grande')
else:
    print('Digite mais de uma letra')