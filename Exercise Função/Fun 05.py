def área(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m².')



print('-' * 30)
print('     Controle de Terrenos  ')
print('-' * 30)
l = float(input('largura (m): '))
c = float(input('Comprimento (m): '))
área(l, c)