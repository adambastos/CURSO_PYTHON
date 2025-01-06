produtos = ["celular", "camera", "fone de ouvido", "monitor"]
for prod in produtos:
    print(prod)
    if prod == "camera": #A execução parará assim que o valor camera for impresso
       break

for i in range(10): #A função range() retorna uma sequência de números, começando em 0 por padrão, e incrementa em 1 (por padrão) e termina em um número especificado.
    print(i)

print('\n')

for x in range(2, 6): #Imprime valores médios de 2 a 6 (mas não incluindo 6):
  print(x)

for r in range(2, 30, 3): #Vai imprimir do dois até o 29, incrementando de 3 em 3, pois o último número que define o intervalo.
    print(r)

for x in range(6):
  print(x)
else:
  print("Finally finished!") #Imprima todos os números de 0 a 5 e imprima uma mensagem quando o loop terminar: