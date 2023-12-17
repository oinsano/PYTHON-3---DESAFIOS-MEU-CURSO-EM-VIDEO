x = int (input('DIGITE UM VALOR: '))
y = int (input('DIGITE OUTRO VALOR: '))
op = 0
while op != 5:
    print('-*' * 10)
    print('[ 1 ] SOMAR')
    print('[ 2 ] MULTIPLICAR')
    print('[ 3 ] MAIOR')
    print('[ 4 ] NOVOS')
    print('[ 5 ] SAIR')
    print('-*' * 10)
    op = int(input(''))
    if op == 1:
        r = x + y
        print('A soma entre {} e {} é igual a {}'.format(x,y,r))
    elif op == 2:
        r = x * y
        print('O produto entre {} e {} é igual a {}'.format(x,y,r))
    elif op == 3:
        if x > y:
            print('O maior é {}'.format(x))
        else:
            print('O maior é {}.'.format(y))
    elif op == 4:
            x = int(input('DIGITE UM VALOR: '))
            y = int(input('DIGITE OUTRO VALOR: '))
    elif op == 5:
        print(' -*-*-*- FIM -*-*-*- ')
    else:
        print('OPCÃO INVALIDA - TENTE NOVAMENTE')
