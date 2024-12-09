#Descobrir a posição da geladeira, e com essa informação descobrir a posição da quantidade de geladeira no estoque

produtos = ['TV', 'CELULAR', 'TABLET', 'MOUSE', 'TECLADO', 'GELADEIRA', 'FORNO']
estoque = [100, 150, 100, 120, 70, 90, 80]

nomeprod = input("Insira o nome do produto: ")

pos = produtos.index(nomeprod)
qnt_estoque = estoque[pos]

if (not nomeprod in produtos):
    print("Este produto não consta na lista.")
elif (nomeprod in produtos):
    print("{} conta na lista de produtos e possui {} unidades em estoque." .format(nomeprod, qnt_estoque))


