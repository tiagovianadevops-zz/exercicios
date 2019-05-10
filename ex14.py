n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2) / 2

if media >= 9:
    conceito = 'A'
    resultado = 'Aprovado'
elif media >= 7.5 and media < 9:
    conceito = 'B'
    resultado = 'Aprovado'
elif media >= 6 and media < 7.5:
    conceito = 'C'
    resultado = 'Aprovado'
elif media >= 4 and media < 6:
    conceito = 'D'
    resultado = 'Reprovado'
elif media < 4:
    conceito = 'E'
    resultado = 'Reprovado'

print('A sua média é: {}'.format(media))
print('Seu conceito foi: {}'.format(conceito))
print('Resultado é: {}'.format(resultado))
