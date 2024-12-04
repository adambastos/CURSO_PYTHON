

vendas = float(input("Qual o seu total de vendas: "))
bonus1 = (15 / 100) * vendas
bonus2 = (10 / 100) * vendas

if (vendas >= 2000):
    print("Parabéns, seu bonus é de 15%, totalizando: R$" + str(bonus1))
elif (vendas >= 1000 and vendas < 2000):
    print("Parabéns, seu bônus é de 10%, totalizando: R$" + str(bonus2))
elif (vendas < 1000):
    print("Você não alcançou a meta!")


