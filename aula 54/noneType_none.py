'''
Valores padrão para parâmentros
Ao definir uma função, os parâmentos podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padão será usado.
Refatorar: editar o seu código.
'''



def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} + {y=} + {z=}', x + y + z)
    else:
        print(f'{x=} + {y=} ', x + y )
soma(1, 2)
soma(5, 3)
soma(100, 200)
soma(9, 7, 0)