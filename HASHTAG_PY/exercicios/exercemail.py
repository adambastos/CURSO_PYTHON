nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
if (not ('@') in email or not nome):
    print("Dados incorretos, por favor preencha corretamente os campos")
else:
    print("Dados corretos.")




