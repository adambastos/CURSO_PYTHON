#Comparar se um produto vende
vendas_produtos = [('iphone', 558147, 951642), 
                   ('galaxy', 712350, 244295), 
                   ('ipad', 573823, 26964), 
                   ('tv', 405252, 787604), 
                   ('máquina de café', 718654, 867660), 
                   ('kindle', 531580, 78830), 
                   ('geladeira', 973139, 710331), 
                   ('adega', 892292, 646016), 
                   ('notebook dell', 422760, 694913), 
                   ('notebook hp', 154753, 539704), 
                   ('notebook asus', 887061, 324831), 
                   ('microsoft surface', 438508, 667179), 
                   ('webcam', 237467, 295633), 
                   ('caixa de som', 489705, 725316), 
                   ('microfone', 328311, 644622), 
                   ('câmera canon', 591120, 994303)]

v_2019 = 0
v_2020 = 0
nome_prod = ''

for item in vendas_produtos:
    nome, v2019, v2020 = item
    if v2020 > v2019:
        nome_prod = nome
        v_2019 = v2019
        v_2020 = v2020
        porcent = ((v2020 - v2019) / v2019) * 100

        print('O produto {} vendeu mais em 2020 em comparação ao ano de 2019, e teve um aumento de {:.1f}%.' .format(nome_prod, porcent))





