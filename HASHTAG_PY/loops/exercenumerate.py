produtos = [
    "Arroz", "Feijão", "Macarrão", "Açúcar", "Café",
    "Óleo", "Sal", "Farinha de trigo", "Leite", "Manteiga",
    "Pão", "Biscoito", "Refrigerante", "Água Mineral", "Sabão em pó",
    "Detergente", "Sabonete", "Shampoo", "Condicionador", "Papel Higiênico"
]
quantidades = [
    50, 40, 30, 60, 20,
    35, 25, 45, 10, 15,
    12, 22, 18, 33, 28,
    36, 24, 19, 17, 50
]

print('Abaixo do mínimo: ')
for i, item in enumerate(quantidades):    
    if item < 20:
        print('Produto: {} / Quantidade: {}' .format(produtos[i], item))

    
        
        
