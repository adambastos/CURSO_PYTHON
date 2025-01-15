#Set serve para remover valores duplicados. No caso o CPF 77772494793 estava duplicado e foi removido. 


cpfs = ['98693685309', '68062113728', '49833784992', '77772494793', '77772494793', '73963474912', '73755258706', '75053472416', '77772494793', '57358277406']

set_cpf = set(cpfs)

print(set_cpf)