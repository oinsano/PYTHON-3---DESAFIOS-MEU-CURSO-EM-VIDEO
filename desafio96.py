def area(l, c):
    a = l * c
    print(f'A area de um tereno {l}x{c} é {a:.2f}m2')


print('Controle de Terrenos')
print('=' * 22)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l ,c)
