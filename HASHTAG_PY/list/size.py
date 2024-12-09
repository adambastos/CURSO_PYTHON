produtos = ['TV', 'CELULAR', 'TABLET', 'MOUSE', 'TECLADO', 'GELADEIRA', 'FORNO']
estoque = [100, 150, 100, 120, 70, 90, 80]
menor = min(estoque)
maior = max(estoque)

pos_menor = estoque.index(menor)
pos_maior = estoque.index(maior)

print(menor)
print(maior)

print(pos_menor)
print(pos_maior)

print('Produto mais caro: {} R$ {} / Produto mais barato: {} R$ {}' .format(produtos[pos_maior], maior, produtos[pos_menor], menor))
