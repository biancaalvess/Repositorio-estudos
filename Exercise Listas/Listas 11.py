teste = list()
teste.append('Bia')
teste.append(24)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1]= 22
galera.append(teste)
print(galera)