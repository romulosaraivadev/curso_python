'''
Listas em python 
Tipo list - Multável
Suporta vários valores de qualquer tipo
Conecimento reutilizáveel - indices e fatiamento
Método úteis: 
    append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, ler, alterar, apager = list[i] (CRUD)
'''
lista = [10,20,30,40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido, ', ultimo_valor)