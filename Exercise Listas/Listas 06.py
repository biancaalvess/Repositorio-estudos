numeros = list()
while True:
    n = int(input('Digite um valor:'))
    if n not in numeros:
        numeros.append(n)
        print('O valor foi adicionado com sucesso...')
    else:
        print(f'O valor foi duplicado, não vou adicionar... ')
    r = str(input('Quer continuar? [S/N]:'))
    if r in 'Nn':
        break
print('-=' * 30)
numeros.sort()
print(f'Você digitou os valores:{numeros}', end='')
