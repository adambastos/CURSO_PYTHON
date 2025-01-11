'''
Exercício 1
Crie um sistema de consulta de preços
Seu sistema deve:
- Pedir para o usuário o nome de um produto
- Caso o produto exista na lista de produtos, o programa deve retornar o preço do produto como resposta
       - Ex: O produto celular custa R$1500
- Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem para o usuário tentar novamente


Exercício 2
Agora edite o programa anterior para fazer com que, caso não exista o produto, o programa pergunte se o usuário quer cadastrar o produto
Se ele responder sim, o programa deve pedir o nome do produto e o preco do produto e cadastrar no dicionário de preços
Em seguida do cadastro bem sucedido, o programa deve printar o dicionário de precos atualizado

'''
precos = {
          "celular": 1500, 
          "camera": 1000, 
          "fone de ouvido": 800, 
          "monitor": 2000
          }

produto = input('Qual o produto a ser consultado? ')

if produto in precos:
    print('O produto {} custa R${}'.format(produto, precos[produto]))
else:
    resp = input('Este produto não existe na lista, deseja adicioná-lo? Digite S ou N ').lower()
    if resp == 'S' or resp == 's':
        nome_prod = input('Digite o nome do produto: ').lower()
        valor_prod = float(input('Digite o valor do produto: '))
        precos[nome_prod] = valor_prod #Adicionando um novo item na lista precos
        print('Produto adicionado com sucesso!')
        for item in precos:
            print('{}: R${:.0f}' .format(item, precos[item]))
    else:
        print('Encerrando!')
        
    


