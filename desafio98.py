from time import sleep
def contador(a, b, c):
    if a > b:
        c *= -1
    if c == 0:
        c = -1
    print('=' * 40)
    print(f'Contagem de {a} até {b} de {c} em {c}')

    for i in range(a, b, c):
        print(f'{i}', end=' ')
        sleep(0)
    print()


contador(1, 10, 1)
contador(10, 0, 2)
print('=' * 40)
print('Agora é a sua vez')
a = int( input('Inicio: '))
b = int( input('Fim: '))
c = int( input('Passo: '))
contador(a, b, c)
