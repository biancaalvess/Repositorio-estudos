largura = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = largura * alt
print('Sua parede tem dimensões de {}x{} e a sua área tem {}m²'.format(largura, alt, area))
tinta = area / 2
print('Para pintar essa parede você vai precisar de {}L de tinta.'.format(tinta))