x = int(input('Quer fatorial de qual numero? '))
f = 1
print('Fatorial de {}'.format(x), end='')
while x != 1:
    f *= x
    x -= 1
print(' é {}.'.format(f))
