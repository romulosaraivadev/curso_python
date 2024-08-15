'''
append - adiciona um item no final
insert - adiciona um item no indece escolhido
pop - remove do final ou do indice escolhido
del - apaga um indice
clear - limpa a lista
extend - estende a lista
+  - concatena lista
'''
lista = [10, 20, 30, 40]
lista.append('romulo')
nome = lista.pop()
lista.append(123)
del lista[-1]
# lista.clear()
lista.insert(10, 5) # 1° valor: qual indece remove. 2° valor: qual valor insere
print(lista)