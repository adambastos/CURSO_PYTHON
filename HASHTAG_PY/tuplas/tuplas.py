tupla = ('Adam', 'Bastos', 'Santos') #As tuplas são imutáveis

name = tupla[0]
middle_name = tupla[1]
last_name = tupla[2]

print('Bem vindo, {} {} {}!' .format(name, middle_name, last_name))

nome, nome_meio, último_nome = tupla #Eu estou atribuindo, em sequência, os elementos da tuplas às variáveis nome, nome_meio e último_nome.
print(nome)