# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

# pessoa = {
#     'nome': 'Romulo',
#     'sobrenome': 'Saraiva',
#     'idade': 29,
# }

# pessoa.setdefault('idade', 0)
# print(pessoa['idade'])
# # print(len(pessoa))
# print(tuple(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))



# # for chave in pessoa.values():
# #     print(chave)

# for chave, valor in pessoa.items():
#     print(chave, valor)
# import copy

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0, 1, 2], 
# }
# d3 = d1.copy()
# d2 = copy.deepcopy(d1)

# d2['c1'] = 1000
# d2['l1'][1] = 99999

# print(d1 )
# print(d2)
# print(d3)


p1 = {
    'nome': 'Romulo',
    'sobrenome': 'Saraiva',
}

# print(p1['nome'])
# print(p1.get('nome', 'não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# sobrenome = p1.popitem()
# print(sobrenome)
# print(p1)
# p1.update({
#     'nome': 'novo valor',
#     'idade': 29
# })
# p1.update(nome='novo valor', idade=29)
tupla = ('nome', 'novo valor'), ('idade', 30)
p1.update(tupla)
print(p1)