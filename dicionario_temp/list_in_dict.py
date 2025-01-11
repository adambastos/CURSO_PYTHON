nomes_produtos = [
    "Notebook",
    "Smartphone",
    "Fone de Ouvido",
    "Teclado",
    "Mouse",
    "Monitor",
    "Impressora",
    "Cadeira Gamer",
    "Mesa de Escritório",
    "Pen Drive"
]


precos_produtos = [
    3500.00, 
    1500.00,  
    250.00,   
    120.00,   
    80.00,  
    800.00,   
    600.00,   
    1200.00, 
    500.00,   
    50.00
]

dicionario = dict.fromkeys(nomes_produtos) #Transforma a lista em dicionário



juntar = zip(nomes_produtos, precos_produtos) #Transformando duas listas distintas em uma lista de tuplas

dicionario2 = dict(juntar) #E aqui eu transformo a lista de tuplas em um dicionário
print(dicionario2)

'''
produtos, preco = zip(dicionario2)
#print('{} está por R${}' .format(produtos, preco))

indice = nomes_produtos.index('Pen Drive')
preco_pendrive = precos_produtos[indice]
#print('O Pen Drive é R${}' .format(preco_pendrive))

'''

