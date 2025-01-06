#4.Em quais meses a média de temperatura foi maior do que a média nacional?
meses = [
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro'
]

temperaturas = [30, 29, 28, 28, 25, 26, 20, 21, 19, 25, 27, 32]

media = sum(temperaturas)/len(temperaturas)
print('{:.1f}'.format(media))

for i, mes in enumerate(meses):
    if temperaturas[i] > media:
        print('O mês {} teve a temperatura acima da média com {} graus' .format(meses[i], temperaturas[i]))

    
    
