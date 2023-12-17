x = y = z = ma = me = 0
c = 'S'
while c == 'S':
    x= int(input('Digite um valor: '))
    y += x
    z += 1
    if z == 1:
        ma = me = x
    else:
        if x > ma:
            ma = x
        if x < me:
            me = x
    c= str(input('Deseja continuar? [S/N] ')).upper().strip()
m = y / z
print('Foram digitados {} valores e a media desses valores = {}'.format(z, m))
print('O menor numero digitado foi {} e o maior numero foi {}.'.format(me, ma))