x = int(input('Digite um numero: '))
y = 0
for c in range (1, x + 1):
    if x % c == 0:
        print('\033[33m', end='')
        y += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(x, y))
if y == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso NÃO é primo')
