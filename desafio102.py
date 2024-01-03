def fatorial(n, show=False):
    f = 1
    print(f'Calculando {n}! = ', end='')
    for i in range(n, 1, -1):
        if show == True:
            print(i, end=' x ')
        f *= i
    if show == True:
        print(f'1 = {f}')
    else:
        print(f'{f}')

n = int(input('Quer saber o fatorial de qual numero? '))
r = str(input('Deseja mostrar resultados [S/N]? ')).upper().strip()[0]
if r == 'S':
    r = True
else:
    r = False
fatorial(n, r)