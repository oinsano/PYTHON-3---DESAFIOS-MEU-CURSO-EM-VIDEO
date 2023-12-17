x = 0
y = 0
p = -1
while x != 999:
    x = int ( input ('Digite um valor: '))
    y += x
    p += 1
c = y - 999
print ('Voce digitou {} valores. A soma dos valores {}.'.format(p, c))
