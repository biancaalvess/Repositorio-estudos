real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 3.27
euro = real / 5.10
print('Com R${:.2f} você pode comprar R$ {:.2f} doláres e R${:.2f} euros. Aproveite e faça uma bela viagem!'.format(real, dolar, euro))
