from random import randint
print('VAMOS JOGAR JOKENPO?')
print('1 - PEDRA \n2 - PAPEL \n3 - TESOURA')
a = int(input('ESCOLHA: '))
b = randint(1, 3)
if a == b:
    print('EMPATE')
elif a == 1 and b == 2:
    print('MAQUINA GANHA')
elif a == 1 and b == 3:
    print('HUMANO GANHA')
elif a == 2 and b == 1:
    print('HUMANO GANHA')
elif a == 2 and b == 3:
    print('MAQUINA GANHA')
elif a == 3 and b == 1:
    print('MAQUINA GANHA')
elif a == 3 and b == 2:
    print('HUMANO GANHA')
else:
    print('INVALIDO')
print('Maquina escolheu {}'.format(b))