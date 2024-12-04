text = "Aqui estou mais um dia"
print(text.upper())
print(text.lower())
print(text.count("i"))
print(text.find("estou")) #Encontrar a posição da palavra dentro da string (Como se fosse um vetor)
print(text.replace("Aqui", "Lá")) #Replace (substituir) "Aqui" por "Lá"
print("chupa" in text) #Verifica se tem a palavra chupa dentro da string text

idade = 26
print("Sua idade é: {}" .format(idade))
print("Sua idade é: " + str(idade)) 
print(f"Sua idade é: {idade}")

text = "Eu estou aqui tendo um ataque"
print(len(text))
print(text[-1]) #Pega o último caracter
print(text[3:8]) #Pega da 3 até a 7 posição

name = "Adam está aqui cansado"
idade = 26
print(name + " tem {} anos." .format(idade)) #Format para formatação de String
print(name.capitalize()) #Deixa a primeira letra da palavra maiúscula
print(name.casefold()) #Deixa todas as letras minúsculas
print(name.count('a')) #Vai contat quantos 'a' tem dentro da String


