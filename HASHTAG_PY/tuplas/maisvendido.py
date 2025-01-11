#Saber qual o produto mais vendido no dia 21/08
vendas = [
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
    ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
    ('21/08/2020', 'iphone x', 'prata', '128gb', 1017, 4000),
    ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000),
]

qnt_mais_vend = 0
nome_mais_vend = ''

for item in vendas:
    data, nome_prod, cor, armazen, qnt_vend, preco = item
    if data == '21/08/2020':
        if qnt_vend > qnt_mais_vend:
            qnt_mais_vend = qnt_vend
            nome_mais_vend = nome_prod

print('{} foi o produto mais vendido com {} unidades.'.format(nome_mais_vend, qnt_mais_vend))