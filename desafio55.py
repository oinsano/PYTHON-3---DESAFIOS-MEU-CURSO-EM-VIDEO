#ler 5 pesos e dizer qual maior e qual menor
a = 0
b = 0
for c in range(1, 6):
    x=float(input('Insira seu peso: '))
    if c == 1:
        a = x
        b = x
    else:
        if x > a:
            a = x
        if x < b:
            b = x
print('O maior peso {}Kg'.format(a))
print('O menor peso {}Kg'.format(b))
