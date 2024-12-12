#Cria uma lista com os m3 maiores valores
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_1sem.extend(vendas_2sem)
vendas_1sem.sort(reverse=True)

final = vendas_1sem[:3]


print('Os melhores meses de vendas: \n' + '\n'.join(map(str, final)))