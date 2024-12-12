# Exercício 3
# Crie um sistema de consulta de bônus dos funcionários
# Seu sistema deve:
# - Pegar o valor de vendas do funcinoário por meio de um input
# - Calcular o bônus do funcionário de acordo com a seguinte regra:
#       - Se o funcionário vendeu mais de 1000 unidades, ele ganha R$2 de bonus para cada unidade vendida
#       - Se o funcionário vendeu mais de 5000 unidades, ele ganha R$2 de bônus para cada unidade + um valor fixo de R$1000
#       - Se o funcionário vendeu menos de 1000 unidades, ele não ganha bônus
# - Printar no final o valor do bônus do funcionário

employer = input('Nome do funcionario: ').upper()
qnt_vendas = int(input('Unidades vendidas: '))

if qnt_vendas > 1000 and qnt_vendas < 5000:
    valor_bonus = qnt_vendas * 2
    print('Bônus de R$ {}' .format(valor_bonus))
elif qnt_vendas > 5000:
    valor_bonus = qnt_vendas * 2 + 1000
    print('Bônus de R$ {}' .format(valor_bonus))
elif qnt_vendas < 1000:
    print('Este funcionário não receberá bônus. ')  
