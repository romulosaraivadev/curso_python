'''
Closure e funções que retornam outras funções
'''
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar



falar_bom_dia = criar_saudacao('bom dia')
falar_boa_noite = criar_saudacao('bom noite')

for nome in ['Maria', 'Joao', 'Romulo']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))