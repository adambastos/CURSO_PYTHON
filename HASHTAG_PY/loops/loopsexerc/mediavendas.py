#### 2. Faça um Programa que crie uma lista com as médias de cada aluno, imprima as médias de cada aluno e a quantidade de alunos com média maior que 7.
alunos = ["José", "Joana", "Maria", "Carla", "Mauricio", "Andre", "Tiago", "Enzo", "Amanda", "Alessandra"]
notas = [
    [10, 9, 8, 8],
    [9, 7, 6, 4],
    [10, 10, 10, 10],
    [5, 3, 10, 9],
    [7, 6, 6, 6],
    [7, 7, 8, 7],
    [7, 7, 7, 9],
    [8, 5, 6, 7],
    [10, 9, 7, 4],
    [10, 1, 3, 3],
]

medias = []
for i in range(len(alunos)):
    media = sum(notas[i]) / len(notas[i])
    medias.append(media)

print('Medias:')
for i in range(len(alunos)):
    print('{}: {}' .format(alunos[i], medias[i]))

acima_media = sum(1 for media in medias if media >7) #Some 1 para cada media in medias que for maior que 7
print('Alunos acima da media: {}' .format(acima_media))



    
    
