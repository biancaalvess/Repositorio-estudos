times = ('Corinthians', 'Palmeiras','Santos','Grêmio',
         'Cruzeiro','Flamengo','Vasco','Chapecoense',
         'Atlético', 'Bota Fogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Viória', 'Coritiba', 'Avai', 'Ponte Preta',
         'Atlético-GO')
print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 primeiros últimos sõa {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética {sorted(times)}')
print('-=' * 15)
print(f'A posição do Chapecoense é {times.index("Chapecoense")+1}º posição')
