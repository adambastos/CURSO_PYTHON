#Transformar as 3 listas em um dicionário

produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]

dict_join = list(zip(vendas2019, vendas2020)) #Primeiro juntar as duas listas vendas
dict_full = dict(zip(produtos, dict_join)) #Depois juntar a junção já feita (dict_join) com com a lista de produtos

print(dict_full)





