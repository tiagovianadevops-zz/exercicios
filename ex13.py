num = int(input('Informe um número que retornaremos o respectivo dia da semana: '))

if num == 1:
   dia ='1 - Domingo'
elif num == 2:
    dia = '2 - Segunda'
elif num == 3:
    dia = '3 - Terça'
elif num == 4:
    dia = '4 - Quarta'
elif num == 5:
    dia = '5 - Quinta'
elif num == 6:
    dia = '6 - Sexta'
elif num == 7:
    dia = '7 - Sabado'
else:
    dia = 'Valor inválido'


print('O dia da semana é:{}'.format(dia))
