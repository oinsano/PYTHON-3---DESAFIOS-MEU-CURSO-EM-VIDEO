def ajuda(comando):
    a = f'ACESSANDO MANUAL DA FUNCÃO {comando}'
    print('\033[45m=' * (len(a) + 4))
    print(f'  {a}')
    print('=' * (len(a) + 4))
    print('\033[m', end='')
    print('\033[30;46m', end='')
    help(comando)
    print('\033[m', end='')



while True:
    a = 'SISTEMA DE AJUDA PyHELP'
    print('\033[44m=' * (len(a) + 4))
    print(f'  {a}')
    print('=' * (len(a) + 4))
    print('\033[m', end='')

    x = str(input('\033[mFuncão ou Biblioteca -->>  '))
    if x == 'fim':
        fim = 'ATÉ LOGO'
        print('\033[30;41m=' * (len(fim) + 4))
        print(f'  {fim}')
        print('=' * (len(fim) + 4))
        break
    ajuda(x)
