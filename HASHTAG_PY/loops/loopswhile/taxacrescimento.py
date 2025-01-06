#4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com 
# uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou 
# iguale a população do país B, mantidas as taxas de crescimento.

a_hab = 80000
b_hab = 200000
tempo = 0

calc_porcent_a = (3 / 100) * a_hab
print('O crescimento populacional anual do país A é de {:.0f} habitantes'.format(calc_porcent_a))

while a_hab < b_hab:
    a_hab *= 1.03
    b_hab *= 1.015
    tempo += 1

print('O país A levará {} anos para alcançar o tamanho populacional do país B.'.format(tempo))

