# Exercício 1
# Crie um sistema de cadastro de produtos em uma lista de produtos
# Seu sistema deve:
# - Pegar o usuário qual produto vai ser cadastrado por meio de um input
# - Garantir que se o usuário escrever com letra maiúscula ou minúscula, o produto continua sendo o mesmo produto
# - Se o usuário inserir um produto que já existe na lista, o programa deve printar a mensagem "Produto já existente, tente novamente"
# - Se o usuário inserir um produto que não existe na lista, o programa deve inserir na lista, printar a mensagem Produto X cadastrado com sucesso e em seguida printar a lista completa

produtos = ["celular", "camera", "fone de ouvido", "monitor"]

prod = input('Digite o nome do produto: ') #Faz com que o texto digitado pelo usuário seja convertido em maiúsculo antes de ser salvo na variável.

if prod in produtos:
    print('Este produto já está cadastrado!')
else:
    alt = input('O produto ainda não está cadastrado, deseja inseri-lo? S ou N')
    alt.upper()

    if alt == 'S':
        newprod = input('Insira o nome do produto: ')
        produtos.append(newprod) 
        print('Produto cadastrado com sucesso! \n')
        print('Lista completa:')
        print('\n'.join(map(str, produtos)))
    

