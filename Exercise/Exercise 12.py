salario = float(input('Qual é o salário do funcionário? R$ '))
novo = salario + (salario * 15 / 100)
print('Um funcionário que ganhava {:.2f}, com 15% passa a receber {:.2f}'.format(salario, novo))