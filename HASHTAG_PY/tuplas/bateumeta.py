meta = 10000
vendas = [
    ('João', 15000),
    ('Julia', 27000),
    ('Marcus', 9900),
    ('Maria', 3750),
    ('Ana', 10300),
    ('Alon', 7870),
]

vend = ''
meta_batida = 0

for item in vendas:
    nome_vend, venda = vendas
    if venda > meta:
        meta_batida = venda
        vend = nome_vend

print('O vendedor {} bateu a meta')