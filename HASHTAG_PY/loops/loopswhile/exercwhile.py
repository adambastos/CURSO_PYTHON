
vendas = []

while True:
    prod = input('Nome do produto: ')
    if not prod:
        break
    qnt = int(input('Quantidade: '))
    vendas.append([prod, qnt])

print(vendas)
