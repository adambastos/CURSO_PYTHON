# 5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

a_hab = int(input('População do país A: '))
b_hab = int(input('População do país B: '))
tax_a = float(input('Taxa de crecimento anual país A: '))
tax_b = float(input('Taxa de crecimento anual país B: '))
tempo = 0

while a_hab < b_hab:
    a_hab *= tax_a
    tempo += 1

print('Habitantes a mais por ano {:.0f}%'.format(a_hab))
print('Quantidade de meses para o pais A alcançar o país B: {}' .format(tempo))