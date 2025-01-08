mais_vendidos = {'tecnologia': 'iphone', 
                 'refrigeracao': 'ar consul 12000 btu', 
                 'livros': 'o alquimista', 
                 'eletrodoméstico': 'geladeira', 
                 'lazer': 'prancha surf'}

vendas_tecnologia = {'iphone': 15000, #Esse
                     'samsung galaxy': 12000, 
                     'tv samsung': 10000, 
                     'ps5': 14300, 
                     'tablet': 1720, 
                     'ipad': 1000, 
                     'tv philco': 2500, 
                     'notebook hp': 1000, 
                     'notebook dell': 17000, 
                     'notebook asus': 2450}

print('Livro mais vendido foi: {}' .format(mais_vendidos['livros']))
print('Ar condicionado mais vendido: {}' .format(mais_vendidos.get('refrigeracao'))) #Buscar utilizando método get

if 'livros' in mais_vendidos:
    print('Realmente existe livros')
else:
    print('Não existe porra nhm')
