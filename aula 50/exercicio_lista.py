'''
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de indices inexistentes na lista.
'''
import os

lista = []
while True:
    print('1. Inserir, 2. Apagar, 3. Listar, 4. Sair')
 
    opcao = input('digite um intem: ')
    
    if opcao == '1':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
        

    elif opcao == '2':
        indice_str = input('Escolha o índice para apagar:')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite um numero inteiro')
        except IndexError:
            print('Índice não existe na lista')
        except:
            print('Erro desconhecido')
    
    elif opcao == '3':
        os.system('cls')

        if len(lista) == 0:
            print('Nada a listar')
        
        for i, valor in enumerate(lista):
            print(i, valor)

    elif opcao == '4':
        print('Voce saiu')
        break
    else:
        print('Digite uma Opção')