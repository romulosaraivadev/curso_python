'''
Exercicio
Peça ao usuario para digitar seu nome
Peça ao usuario para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        seu nome é {nome}
        seu nome invertido é {nome invertido}
        se seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A ultima letra do seu nome é {letra}
se nada for digitado em nome ou idade:
    exiba "desculpe, voce deixou campos vazios."
'''

nome = input('Digite seu nome: ')
idade = input('Digite sua altura: ')
nome_invertido = nome[-1::-1]


if not nome or not idade:
    print('Desculpa, você deixou campos vazios')
else:
    print(f'Seu nome é {nome}.')
    print(f'Seu nome invertido é {nome_invertido}')

    if ' ' in nome:
        print('Seu nome contem espaço')
    else:
        print('Seu nome não contem espaço')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')