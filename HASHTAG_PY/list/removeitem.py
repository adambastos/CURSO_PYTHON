produtos = ['TV', 'CELULAR', 'TABLET', 'MOUSE', 'TECLADO', 'GELADEIRA', 'FORNO']
produtos.append('FRITADEIRA') #Adiciona um item na lista
#produtos.remove('TV') #Remove

item_removido = produtos.pop(2) #A diferença do REMOVE para o POP é que com o POP, você consegue armazenar o item removido em uma variável
print(produtos)
print(item_removido)