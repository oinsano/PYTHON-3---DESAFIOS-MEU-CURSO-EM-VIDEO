a = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão: '))
d = a + (10 - 1) * r
for c in range(a, d + r, r):
        print('{}'.format(c), end=(' - '))
print('ACABOU')