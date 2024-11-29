names = ["Adam", "Bastos", "Santos"]

for name in names: #Para cada name em names, imprima name.
    print(name)

numbers = [1, 2, 3, 4, 5, 6]
numbers.insert(0, -1) #Insira o número -1 na posição 0 do vetor.
numbers.remove(4) #Remove o número 4 da lista, e não o elemento na quarta posição
print(numbers)

print(10 in numbers) #Verifica se há o número 10 dentro de numbers e retorna um booleano
