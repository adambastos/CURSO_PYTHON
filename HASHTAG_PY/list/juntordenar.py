lista1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
lista2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

lista1.extend(lista2) #Juntando duas listas
print(lista1)

lista1.sort(reverse=True) #Reverte a ordem da lista
print(lista1)

print("\n".join(map(str, lista1))) #Imprimindo itens da lista sem os colchetes e com outra formatação (a critério)



