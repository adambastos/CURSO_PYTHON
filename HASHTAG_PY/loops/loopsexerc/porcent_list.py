"""
# Exercícios

## 1. Calculando % de uma lista

Faremos algo parecido com "filtrar" uma lista. Mais pra frente no curso aprenderemos outras formas de fazer isso, mas com o nosso conhecimentoa atual já conseguimos resolver o desafio.

Digamos que a gente tenha uma lista de vendedores e ao invés de saber todos os vendedores que bateram a meta, eu quero conseguir calcular o % de vendedores que bateram a meta. 
Ou seja, se temos 10 vendedores e 3 bateram a meta, temos 30% dos vendedores que bateram a meta.
"""
meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

qnt_vend = len(vendas)
bateu_meta = []

for venda in vendas:
    if venda[1] >= meta:
        bateu_meta.append(venda)
        porcent = len(bateu_meta) / len(vendas)
print('{:.0%} dos vendedores bateram a meta' .format(porcent)) #O .0 indica que você não quer nenhuma casa após a vírgula

#Testando o {:.0%}
v1 = 100
v2 = 50
calc = v2 / v1
print('{:.0%}' .format(calc)) # % informa que o número deve se formatado como uma porcentagem




        
        
#print('A porcentagem de vendedores que bateram a meta é de {:.2f}%' .format(porcent))