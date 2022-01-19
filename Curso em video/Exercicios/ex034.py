salario = float(input('Qual é o salário do funcionário?'))
if salario > 1250.00:
    ajuste = salario * 1.1
else:
    ajuste = salario * 1.15
print('O seu salário era de {:.2f}, seu novo salário é de R$ {:.2f}'.format(salario, ajuste))