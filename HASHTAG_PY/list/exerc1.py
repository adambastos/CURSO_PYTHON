meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_1sem.extend(vendas_2sem)

menor_v = min(vendas_1sem)
maior_v = max(vendas_1sem)


pos_min = vendas_1sem.index(menor_v)
pos_max = vendas_1sem.index(maior_v)


print("O mês mais fraco de vendas foi: {} com R$ {} em vendas." .format(meses[pos_min], menor_v))
print("O mês mais forte de vendas foi: {} com R$ {} em vendas." .format(meses[pos_max], maior_v))




