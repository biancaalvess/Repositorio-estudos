import math
an = float(input('Digita o angulo que você deseja: '))
seno = math.sin(math.radians(an))
print('O ângulo {:.2f} temo SENO de {:.2f}'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('O ângulo {:.2f} do COSSENO é de {:.2f}'.format(an, cosseno))
tangente = math.tan(math.radians(an))
print('O angulo de {:.2f} da TANGENTE é de {:.2f}'.format(an, tangente))
