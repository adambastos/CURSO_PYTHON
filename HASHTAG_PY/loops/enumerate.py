#Função embutida usada para iterar sobre uma sequência (como uma lista, tupla ou string), retornando tanto o índice de cada item quanto o próprio item.

pessoas = ['Adam', 'Gustavo', 'Laura', 'Victoria']
for i, item in enumerate(pessoas): #Uso a variável i para pegar o índice e e item para pegar o item.
    print(i, item)

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
for produto, quantidade in zip(produtos, quantidades): #O loop zip é usado para combinar os dois, permitindo exibir o nome do produto junto com sua quantidade em estoque.
    print(f"{produto}: {quantidade} unidades em estoque")