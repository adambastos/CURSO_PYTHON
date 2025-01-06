#3. Foram anotadas as idades e salários de 30 funcionários. Faça um programa que determine quantos funionários com mais de 25 anos possuem o salário inferior à média de todos os salários.

idades = [35,32,50,33,48,50,33,48,22,49,35,38,20,47,49,48,34,21,48,44,48,30,25,42,42,23,25,23,38,35]
salarios = [3739,2219,3554,3978,4014,3270,4792,3879,2981,2384,4826,2460,3680,4318,1872,1770,4640,3929,3295,1729,3965,4267,4007,1916,2987,2943,3852,4543,2055,1730]

for i in range(len(salarios)):
    media_sal = sum(salarios) / len(salarios)
print('Média salarial: R${:.2f}'.format(media_sal))

for i in range(len(idades)):
    idade_maior = sum(1 for age in idades if age > 25)
    
print('Funcionários com mais de 25: {}'.format(idade_maior))

for i, func in enumerate(idades):
    sal_inf = sum(1 for sal in salarios[i] < media_sal and idades[i] > 25)
print(sal_inf)



