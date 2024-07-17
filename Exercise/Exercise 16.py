import math
co = float(input('Qualo cumprimento do cateto oposto: '))
ca = float(input('Qual o cumprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))


#não funciona