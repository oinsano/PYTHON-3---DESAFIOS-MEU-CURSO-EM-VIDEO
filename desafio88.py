from random import randint
from time import sleep
print('-' * 40)
print('- - - - - - JOGO DA MEGA SENA - - - - - -')
print('-' * 40)
x = int(input('Quantos jogos você quer que eu sortei? '))
print(f'>>>>>>>>>> Sorteando {x} jogos <<<<<<<<<<')
sleep(0.1)
for i in range(1, x+1):
    c = 0
    j = []
    while True:
        r = randint(1, 60)
        if r not in j:
            j.append(r)
            c +=1
        if c == 6:
            break
    print(f'Jogo {i}: {sorted(j)}')
    sleep(0.5)
print('>>>>>>>>>> BOA SORTE <<<<<<<<<<')
