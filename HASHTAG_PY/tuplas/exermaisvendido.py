#Para saber o total de faturamento geral no dia 21/08
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

faturamento = 0
for item in vendas:
    data, nome_prod, cor, armazen, qnt_vend, preco = item
    if data == '21/08/2020' and nome_prod == 'iphone x': 
        faturamento += qnt_vend * preco 

print('A quantidade de vendas do dia 21/08/2020 foi de {}' .format(faturamento))