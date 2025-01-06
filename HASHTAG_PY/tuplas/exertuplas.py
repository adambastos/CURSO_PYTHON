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

#Supondo que queiramos saber o faturamento de cada dispositivo. Com o for, seria feito da seguinte forma
x = 0
for i, venda in enumerate(vendas):
    total_vendas = vendas[x][4] * vendas[x][5]
    print('{}'.format(total_vendas))
    x += 1

#Utilizando a tupla fica assim
for ind, venda in enumerate(vendas):
    data_venda, modelo, cor, armaze, qnt_vend, preco = venda
    total_vendas_tup = qnt_vend * preco  # Multiplica quantidade vendida pelo preço
    print(f"Item {ind + 1}: Modelo: {modelo}, Cor: {cor}, Total de Vendas: R$ {total_vendas_tup:.2f}")

