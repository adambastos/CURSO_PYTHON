#FOR para pegar a chave e o valor de um dicionários
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

for chave in vendas_2025:
        print('{}: {}' .format(chave, vendas_2025[chave])) #para pegar o valor de um item, você utiliza o nome do dicionario mais a variável do for; 


