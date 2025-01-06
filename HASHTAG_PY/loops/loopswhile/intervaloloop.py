#1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

num = int(input('Insira uma nota: '))

while num:
    if num < 0 or num >10:
        print('Nota inválida:')
        num = int(input('Insira uma nota: '))
    else:
        print('Nota válida.')
        break
        


