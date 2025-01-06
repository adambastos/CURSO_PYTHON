# 3. Faça um programa que leia e valide as seguintes informações (e para cada uma delas, continue pedindo a informação até o usuário inserir corretamente):
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

name = input('Nome: ')
age = int(input('Idade: '))
salary = float(input('Salário: '))
sexo = input('Sexo: ')
est_civ = input('Estado Civil: ')

while True:
    if len(name) > 3 and age > 0 and age <= 150 and salary > 0 and sexo == 'm' or sexo == 'f':
        print('Dados válidos.')
        break
    elif est_civ in ['s', 'c', 'v', 'd']:
        print('Dados válidos.')
        break
    else:
        print('Um dos campos foi digitado incorretamente, por favor preencha novamente.')
        name = input('Nome: ')
        age = int(input('Idade: '))
        salary = float(input('Salário: '))
        sexo = input('Sexo: ').lower()
        est_civ = input('Estado Civil: ').lower()


