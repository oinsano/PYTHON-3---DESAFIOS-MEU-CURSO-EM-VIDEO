import random
c = 1
x = random.randint(0, 10)
y= int(input('Adivinhe o numero entre 0 e 10: ' ))
while x != y:
    y = int(input('Tente novamente: '))
    c += 1
if x == y:
    print('Você GANHOU!!!')
    print('Você precisou de {} tentativas.'.format(c))
else:
    print('Você perdeu.')
