'''

Exercício 5
- Uma empresa está analisando os resultados de vendas do 1º semestre de 2022 e 2023
- Qual foi o % de crescimento de cada mês de 2023 em relação a 2022?
- Depois de calcular isso, calcule o valor total de crescimento de 2023 em relação a 2022

'''
vendas_22 = {"jan": 15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai": 16300, "jun": 17000}
vendas_23 = {"jan": 17000, "fev": 15000, "mar": 17500, "abr": 16900, "mai": 16000, "jun": 18500}

list23 = list(vendas_23.items())
list22 = list(vendas_22.items())



i = 0

for i in range(len(list22)):
    if list23[i][1] > list22[i][1]:
        porcent = (list23[i][1] - list22[i][1]) / list22[i][1] * 100
        aument = list23[i][1] - list22[i][1]
        print('O mês de {} foi melhor em 2023. Teve um crescimento de {:.1f}%, e um aumento nas vendas de {:.2f} reais em relação a 2022.' .format(list23[i][0], porcent, aument))
        i += 1
    else:
        maisvendas = list22[i][1] - list23[i][1]
        print('O mês de {} foi melhor em 2022 com R${} a mais em vendas.' .format(list22[i][0], maisvendas))


