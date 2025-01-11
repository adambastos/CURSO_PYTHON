vendas_tecnologia = {'iphone': 15000, 
                     'samsung galaxy': 12000, 
                     'tv samsung': 10000, 
                     'ps5': 14300, 
                     'tablet': 1720, 
                     'ipad': 1000, 
                     'tv philco': 2500, 
                     'notebook hp': 1000, 
                     'notebook dell': 17000, 
                     'notebook asus': 2450}

items = vendas_tecnologia.items()
#print('\n' .join(map(str, items)))

for prod, qnt in vendas_tecnologia.items(): #Fazendo o unpacking do dicionário
    if qnt >= 10000:
        print('{}: {} unidades'.format(prod, qnt))

chaves = vendas_tecnologia.keys()
values = vendas_tecnologia.values()
#print('\n '.join(map(str, chaves)))

lista = list(vendas_tecnologia) #Transformar o dicionário em lista para facilitar visualização e manuseio
lista.sort(reverse='true')
print(lista)
