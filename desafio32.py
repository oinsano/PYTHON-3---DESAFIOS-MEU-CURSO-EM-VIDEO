x = int (input('Escreva um ano: ') )
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print('ANO BISSEXTO')
else:
    print('Ano não bissexto')
