#Adicionar itens no dicionário

mais_vendidos = {'tecnologia': 'iphone', 
                 'refrigeracao': 'ar consul 12000 btu', 
                 'livros': 'o alquimista', 
                 'eletrodoméstico': 'geladeira', 
                 'lazer': 'prancha surf'}


#Update > Melhor forma quando se quer adicionar mais de um item de uma vez
mais_vendidos.update({'cosmeticos': 'Mamae Bebe'})
#print(mais_vendidos)

#Outra forma > Primeiro vem a chave "Limpeza" e depois o valor 'Sabao OMO'
mais_vendidos['limpeza'] = 'Sabao OMO'
#print(mais_vendidos)

vendas_1sem = {
    "Janeiro": 120,
    "Fevereiro": 95,
    "Março": 110,
    "Abril": 130,
    "Maio": 150,
    "Junho": 140
}
vendas_2sem = {
    "Julho": 135,
    "Agosto": 160,
    "Setembro": 155,
    "Outubro": 170,
    "Novembro": 180,
    "Dezembro": 200
}

print(vendas_1sem)

#juntando as duas listas
vendas_1sem.update(vendas_2sem)
print(vendas_1sem)


#Remover itens
vendas_2025 = {
    "Janeiro": 125,
    "Fevereiro": 100,
    "Março": 115,
    "Abril": 135,
    "Maio": 155,
    "Junho": 145,
    "Julho": 140,
    "Agosto": 165,
    "Setembro": 160,
    "Outubro": 175,
    "Novembro": 185,
    "Dezembro": 205
}
#Apenas deletando o item da lista
del vendas_2025['Março']
print(vendas_2025)

#Removendo a chave Dezembro e armazenando seu valor na variável excluido
excluido = vendas_2025.pop('Dezembro')
print(vendas_2025)
print(excluido)