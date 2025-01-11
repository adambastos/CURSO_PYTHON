meta = 10000
vendas = [
    ('João', 15000),
    ('Julia', 27000),
    ('Marcus', 9900),
    ('Maria', 3750),
    ('Ana', 10300),
    ('Alon', 7870),
]

nome = ''
qnt_venda = 0

for item in vendas:
    nome_v, venda = item
    if venda > meta:
        qnt_venda = venda
        nome = nome_v
        print('O vendedor {} bateu a meta com R${} em vendas.' .format(nome, qnt_venda)) 

