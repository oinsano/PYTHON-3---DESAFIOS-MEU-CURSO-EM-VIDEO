import random
x = random.randint(0, 5)
y= int(input('Adivinhe o numero entre 0 e 5: ' ))
if x == y:
    print('Você GANHOU!!!')
else:
    print('Você perdeu.')