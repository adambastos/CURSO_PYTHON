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

#Em dicionários, pegamos os dados pelo nome da chave. EX: Quero o número de vendas do iphone
qnt_vendas = vendas_tecnologia['iphone']
print(qnt_vendas)

#O item mais vendido de tecnologia
tecno = mais_vendidos['tecnologia']
print(tecno)