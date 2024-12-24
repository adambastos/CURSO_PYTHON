#### 1. Faça um Programa que leia as vendas dos vendedores, mostre a venda de cada vendedor com o seu nome e a média de vendas. 

vendas = [1000, 1500, 1200, 1300]
vendedores = ["Fulano", "Beltrano", "Ciclano", "Lira"]

for i, venda in enumerate(vendas):
    pos = i  
    vendor = vendedores[pos]
    media = sum(vendas) / len(vendas)
    print('{} vendeu {} unidades.' .format(vendor, venda))
print('A média de vendas foi de {:.0f}' .format(media)) 
    