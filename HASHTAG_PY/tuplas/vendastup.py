def bateumeta(vendas):
    meta = 10000
    bateram_eta = []
    for venda in vendas:
        nome, valor = venda
        if valor > meta:
            bateram_eta.append({"nome": nome, "valor": valor})
    return bateram_eta
     
vendas = [
    ('João', 15000),
    ('Julia', 27000),
    ('Marcus', 9900),
    ('Maria', 3750),
    ('Ana', 10300),
    ('Alon', 7870),
]

resultado = bateumeta(vendas)

for vendedor in resultado:
    print('{} bateu a meta com R${} em vendas.' .format(vendedor['nome'], vendedor['valor']))



