slatual = float(input('Informe seu salário atual R$ '))

if slatual <= 280:
    aumento = (slatual * 20) / 100
    salario = aumento + slatual
    perc = 20
if slatual > 280 and slatual < 700:
    aumento = (slatual * 15) / 100
    salario = aumento + slatual
    perc = 15
if slatual > 700 and slatual < 1500:
    aumento = (slatual * 10) / 100
    salario = aumento + slatual
    perc = 10
if slatual > 1500:
    aumento = (slatual * 5) / 100
    salario = aumento + slatual
    perc = 5
print('O salário antes do Resjuste é de R${:.2f}'.format(slatual))
print('O percentual de aumento aplicado é de {}%'.format(perc))
print('O valor do aumento é R${:.2f}'.format(aumento))
print('O novo salário é R${:.2f}'.format(salario))
