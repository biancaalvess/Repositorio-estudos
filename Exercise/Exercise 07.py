medida = float(input('Uma distância em metros: '))
cm = medida * 100
nm = medida * 1000
print('A medida de {:.0f} corresponde a {:.0f}nm e {:.0f}cm'.format(medida, cm, nm))