vendedores = ['Adam', 'Gustavo', 'Frank', 'Matheus']
produtos = ['Ipad', 'Iphone']
vendas = [
    [100, 200],
    [300, 500],
    [50, 1000],
    [900, 10]
]

vendas_ipad_gustavo = vendas[1][0] #Quantidade de vendas de Ipad do Gustavo é a lista que está na posição 1, e dentro da lista 1 na posição 0 
print(str(vendas_ipad_gustavo))

vendas_iphone_matheus = vendas[3][1]
print(str(vendas_iphone_matheus))

vendas_iphone = vendas[0][1] + vendas[1][1] + vendas[2][1] + vendas[3][1]
print('Quantidade de vendas de Iphone: ' + str(vendas_iphone))

vendas_mac = [10, 15, 6, 70]
vendas[0].append(vendas_mac[0]) #Adicionando as vendas de mac na lista vendas > Na lista de posição 0 em vendas, eu adiciono o item de posição 0 da lista vendas_mac
vendas[1].append(vendas_mac[1])
vendas[2].append(vendas_mac[2])
vendas[3].append(vendas_mac[3])



print(vendas)