#mostrar [milha, cnetena, dezena e unidade]
x= int (input('digite um numero entre 0 - 9999 '))
u = x // 1 % 10
d = x // 10 % 10
c = x // 100 % 10
m = x // 1000 % 10
print('MILHAS - {}'.format(m))
print('CENTENAS - {}'.format(c))
print('DEZENAS - {}'.format(d))
print('UNIDADES - {}'.format(u))