from random import randint
from time import sleep
def maior(* num):
    c = maior = 0
    print('Analisando Valores . . . . . . .')
    for i in num:
        print(i, end=' ')
        sleep(0.2)
        if c == 0:
            maior = i
        else:
            if i > maior:
                maior = i
        c += 1
    print(f'Foram informados {len(num)} valores')
    print(f'O maior valor informado foi {maior}')
    print('=*' * 20)


maior(randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
maior(randint(0,10), randint(0,10), randint(0,10), randint(0,10))
maior(randint(0,10), randint(0,10))
maior(randint(0,10), randint(0,10), randint(0,10))
maior()