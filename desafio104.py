def leiaint(a):
    ok =False
    v = 0
    while True:
        x = str(input(f'{a}'))
        if x.isnumeric():
            v = int(x)
            ok = True
            return x
            break
        else:
            print('\033[31mERRO! Digite um numero valido\033[m')


while True:
    x = leiaint('Digite um numero: ')
    print(f'Você digitou o numero {x}.')
    if x == 999:
        break
