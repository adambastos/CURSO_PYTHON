'''
Vamos criar um sistema de vendas. Nosso programa deve registrar os produtos e as quantidades (2 inputs) e adicionar em uma lista.

O programa deve continuar rodando até o input ser vazio, ou seja, o usuário apertar enter sem digitar nenhum produto ou quantidade.

Ao final do programa, ele deve printar todos os produtos e quantidades vendidas.

Obs: Caso queira, para o print ficar mais visual, pode usar o join para cada item ser printado em uma linha.
Sugestão para sua lista de produtos vendidos:

'''

vendas = []
while True:
    prod = input('Nome do produto: ')
    if not prod:
        print('Produto inválido.')
        break
    qnt = int(input('Quantidade: '))
    vendas.append([prod, qnt])    
        
print(vendas)



