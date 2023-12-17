p = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão: '))
c = 1
t = 0
m = 10
while m != 0:
    t = t + m
    while c <= t:
        print('{} -> '.format(p), end='')
        p += r
        c +=1
    print('PAUSA')
    m = int (input('Mais quantos termos você quer ver? '))
print('ACABOU')
print('Foram mostrados {} termos'.format(t))