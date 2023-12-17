p = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão: '))
c = 1

while c <= 10:
        print('{} -> '.format(p), end='')
        p += r
        c +=1
print('ACABOU')