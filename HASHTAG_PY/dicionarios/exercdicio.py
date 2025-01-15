#somar o valor de todos os notebooks dentro do dicionario
vendas_tecnologia = {'iphone': 15000, 
                     'samsung galaxy': 12000, 
                     'tv samsung': 10000, 'ps5': 14300, 
                     'tablet': 1720, 'ipad': 1000, 
                     'tv philco': 2500, 
                     'notebook hp': 1000, 
                     'notebook dell': 17000, 
                     'notebook asus': 2450}

total_not = 0
for chave in vendas_tecnologia:
    if 'notebook' in chave:
        total_not += vendas_tecnologia[chave]

print('O total de vendas de notebook foi de: R${}' .format(total_not))