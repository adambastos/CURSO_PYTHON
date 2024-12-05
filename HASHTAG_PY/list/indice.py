#Descobrir a posição da geladeira, e com essa informação descobrir a posição da quantidade de geladeira no estoque

produtos = ['TV', 'CELULAR', 'TABLET', 'MOUSE', 'TECLADO', 'GELADEIRA', 'FORNO']
estoque = [100, 150, 100, 120, 70, 90, 80]

pos = produtos.index('GELADEIRA')
qnt_estoque = estoque[pos]
print(pos)
print(qnt_estoque)


nomeprod = input("Insira o nome do produto: ")
if (not nomeprod in produtos):
    print("Este produto não existe na lista.")
elif (nomeprod in produtos):
    print("{} conta na lista de produtos." .format(nomeprod))