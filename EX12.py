vlhora = int(input('Qual o valor da sua hora de trabalho R$ '))
qtdhora = int(input('Quantas horas trabalhadas no mês: '))

bruto = vlhora * qtdhora

if bruto <= 900:
    perc = 0
    ir = 0
    inss = (bruto * 10) / 100
    fgts = (bruto * 11) / 100
    descontos = inss + ir
    salario = bruto - descontos
if bruto > 900 and bruto <= 1500:
    perc = 5
    ir = (bruto * perc) / 100
    inss = (bruto * 10) / 100
    fgts = (bruto * 11) / 100
    descontos = inss + ir
    salario = bruto - descontos
if bruto > 1500 and bruto <= 2500:
    perc = 10
    ir = (bruto * perc) / 100
    inss = (bruto * 10) / 100
    fgts = (bruto * 11) / 100
    descontos = inss + ir
    salario = bruto - descontos
if bruto > 2500:
    perc = 20
    ir = (bruto * perc) / 100
    inss = (bruto * 10) / 100
    fgts = (bruto * 11) / 100
    descontos = inss + ir
    salario = bruto - descontos

print('Salário Bruto:  ({} * {})         : R${:.2f}'.format(vlhora, qtdhora, bruto))
print('(-) IR ({}%)                      : R${:.2f}'.format(perc, ir))
print('(-) INSS (10%)                    : R${:.2f}'.format(inss))
print('FGTS (11%)                        : R${:.2f}'.format(fgts))
print('Total de descontos                : R${:.2f}'.format(descontos))
print('Salário Liquido                   : R${:.2f}'.format(salario))
