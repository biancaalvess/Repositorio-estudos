num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
s = num // 100 % 10
m = num // 1000 % 10
print('Análisando o número {}...'.format(num))
print('Unidadde {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(s))
print('Milhar {}'.format(m))
