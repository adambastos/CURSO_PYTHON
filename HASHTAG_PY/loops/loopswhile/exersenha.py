#2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

name = input('Nome: ')
passw = input('Senha: ')

while True:
    if passw == name:
        print('Senha inválida, preencha novamente os dados!')
        name = input('Nome: ')
        passw = input('Senha: ')
    else:
        print('Dados cadastrados com sucesso.')
        break
        